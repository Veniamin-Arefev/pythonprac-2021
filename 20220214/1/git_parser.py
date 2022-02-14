import zlib
import sys
from glob import iglob
from os.path import join

from colorama import Fore, Back, Style

repo = sys.argv[1]
repo_path = join(repo, 'objects', '??', '*')

for obj_name in iglob(repo_path):
    print(Fore.GREEN, obj_name, Fore.RESET)

    with open(obj_name, 'rb') as file:
        full_obj = zlib.decompress(file.read())
        header, _, body = full_obj.partition(b'\x00')
        kind, size = header.split()
        print(Fore.BLUE, kind.decode(), int(size), Fore.RESET)
        if kind == b'commit':
            print(body.decode())
        elif kind == b'tree':
            while body:
                treehdr, _, tail = body.partition(b'\x00')
                gitid, body = tail[:20], tail[20:]
                print(f'\t{treehdr}, {gitid.hex()}')
        elif kind == b'blob':
            print("There must be info about blob")
        else:
            print(Fore.RED, "ERROR TYPE", Fore.RESET)
