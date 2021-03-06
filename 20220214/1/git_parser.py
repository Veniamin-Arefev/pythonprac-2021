import argparse
import os
import zlib
import sys
from glob import iglob
from os.path import join

try:
    from colorama import Fore, Back, Style
except BaseException as e:
    print(e)
    print('Please execute "pip install colorama"')
    exit(0)

prefix = '.git'
commit_step = 2
tree_step = 2

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--blob',
                    action='store_true',
                    help='Print all blobs info',
                    )
parser.add_argument('-t', '--tree',
                    action='store_true',
                    help='Parse all tree object recursive',
                    )

args = parser.parse_args()
print(args)


def parse_obj(id: str, intendant: int):
    obj_name = join(prefix, 'objects', id[:2], id[2:])
    print(f'{" " * intendant}{Fore.GREEN}Item id: {id}{Fore.RESET}')

    with open(obj_name, 'rb') as file:
        full_obj = zlib.decompress(file.read())
        header, _, body = full_obj.partition(b'\x00')
        kind, size = header.split()
        print(f'{" " * intendant}{Fore.BLUE}Type : {kind.decode():8} with {int(size):5} bytes{Fore.RESET}')

        pref = ' ' * intendant
        if kind == b'commit':
            text = body.decode()
            print('\n'.join(map(lambda x: pref + x, text.split('\n'))))
            for item in text.split('\n'):
                try:
                    new_kind, new_id = item.split()
                    if new_kind == 'tree':
                        parse_obj(new_id, intendant)
                    elif new_kind == 'parent':
                        parse_obj(new_id, intendant + commit_step)
                        break
                except ValueError:
                    break
        elif kind == b'tree':
            while body:
                treehdr, _, tail = body.partition(b'\x00')
                gitid, body = tail[:20], tail[20:]
                print(f'{pref}{treehdr}, {gitid.hex()}')
                if args.tree:
                    parse_obj(gitid.hex(), intendant + tree_step)
        elif kind == b'blob':
            if (args.blob):
                print(body.decode())
            else:
                pass
                # print(f'{pref}There must be info about blob')
        else:
            print(f'{pref}{Fore.RED}ERROR TYPE{Fore.RESET}')


branches = os.listdir('.git/refs/heads')

if len(sys.argv) <= 1:
    print(f'{Fore.RED}Target branch not specified.{Fore.RESET} Possible variants is {", ".join(branches)}. '
          f'Switching to {Fore.CYAN}{(branch_name := branches[0])}{Fore.RESET}.')
else:
    if sys.argv[1] not in branches:
        print(f'{Fore.RED}Target branch not found.{Fore.RESET} Possible variants is {", ".join(branches)}. '
              f'Switching to {Fore.CYAN}{(branch_name := branches[0])}{Fore.RESET}.')
    else:
        print(f'Parsing {(branch_name := sys.argv[1])} branch.')

with open(join(prefix, 'refs', 'heads', branch_name), 'r') as file:
    commit_id = file.read().strip()

parse_obj(commit_id, 0)
