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

branches = os.listdir(".git/refs/heads")

if len(sys.argv) <= 1:
    print(f"{Fore.RED}Target branch not specified.{Fore.RESET} Possible variants is {', '.join(branches)}. "
          f"Switching to {Fore.CYAN}{(repo := branches[0])}{Fore.RESET}.")
else:
    if sys.argv[1] not in branches:
        print(f"{Fore.RED}Target branch not found.{Fore.RESET} Possible variants is {', '.join(branches)}. "
              f"Switching to {Fore.CYAN}{(repo := branches[0])}{Fore.RESET}.")
    else:
        print(f"Parsing {(repo := sys.argv[1])} branch.")

# repo_path = join(repo, 'objects', '??', '*')

# for obj_name in iglob(repo_path):
#     print(Fore.GREEN, obj_name, Fore.RESET)
#
#     with open(obj_name, 'rb') as file:
#         full_obj = zlib.decompress(file.read())
#         header, _, body = full_obj.partition(b'\x00')
#         kind, size = header.split()
#         print(Fore.BLUE, kind.decode(), int(size), Fore.RESET)
#         if kind == b'commit':
#             print(body.decode())
#         elif kind == b'tree':
#             while body:
#                 treehdr, _, tail = body.partition(b'\x00')
#                 gitid, body = tail[:20], tail[20:]
#                 print(f'\t{treehdr}, {gitid.hex()}')
#         elif kind == b'blob':
#             print("There must be info about blob")
#         else:
#             print(Fore.RED, "ERROR TYPE", Fore.RESET)
