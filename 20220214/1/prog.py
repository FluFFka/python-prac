import sys
from os import listdir
from os.path import join
from glob import iglob
import zlib

repo_path = join('..', '..')
branches_path = join(repo_path, '.git', 'refs', 'heads')

def get_object_info(repo_path, object_id):
    object_path = join(repo_path, '.git', 'objects', object_id[0:2], object_id[2:])
    with open(object_path, 'rb') as object_file:
        dec = zlib.decompress(object_file.read())
        header, _, body = dec.partition(b'\x00')
        kind, _ = header.split()
    return kind, body

if len(sys.argv) <= 1:
    print(', '.join(listdir(branches_path)))
else:
    branch_name = sys.argv[1]
    branch_path = join(branches_path, branch_name)
    with open(branch_path, "r") as f:
        branch_id = f.read().strip()
    _, commit_body = get_object_info(repo_path, branch_id)
    commit_info = commit_body.decode()
    print(commit_info)
    tree_id = commit_info.split()[1]
    _, tree_body = get_object_info(repo_path, tree_id)
    
    tail = tree_body
    while tail:
        treeobj, _, tail = tail.partition(b'\x00')
        tmode, tname = treeobj.split()
        num, tail = tail[:20], tail[20:]
        print(f"{tname.decode()} {tmode.decode()} {num.hex()}")
