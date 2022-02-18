import sys
from os import listdir
from os.path import join
from glob import iglob
import zlib

repo_path = join('..', '..')
branches_path = join(repo_path, '.git', 'refs', 'heads')

if len(sys.argv) <= 1:
    print(', '.join(listdir(branches_path)))
else:
    branch_name = sys.argv[1]
    branch_path = join(branches_path, branch_name)
    with open(branch_path, "r") as f:
        branch_id = f.read().strip()
    last_commit_path = join(repo_path, '.git', 'objects', branch_id[0:2], branch_id[2:])
    with open(last_commit_path, 'rb') as commit_file:
        commit_dec = zlib.decompress(commit_file.read())
        header, _, body = commit_dec.partition(b'\x00')
        kind, size = header.split()
        if kind == b'commit':
            print(body.decode())
