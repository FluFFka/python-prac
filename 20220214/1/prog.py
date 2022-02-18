import sys
from os import listdir
from os.path import join
from glob import iglob
import zlib

repo_path = join('..', '..')
branches_path = join(repo_path, '.git', 'refs', 'heads')
SHIFT = "    "

def get_object_info(repo_path, object_id):
    object_path = join(repo_path, '.git', 'objects', object_id[0:2], object_id[2:])
    with open(object_path, 'rb') as object_file:
        dec = zlib.decompress(object_file.read())
        header, _, body = dec.partition(b'\x00')
        kind, _ = header.split()
    return kind, body

def draw_tree(repo_path, tree_id, level=0):
    _, tail = get_object_info(repo_path, tree_id)
    while tail:
        tree_object, _, tail = tail.partition(b'\x00')

        tmode, tname = tree_object.split()
        num, tail = tail[:20], tail[20:]
        print(f"{SHIFT*level}{tname.decode()} {tmode.decode()} {num.hex()}")
        if tmode == b'40000':
            draw_tree(repo_path, num.hex(), level + 1)

def commit_story(repo_path, commit_id):
    while 1:
        _, commit_body = get_object_info(repo_path, commit_id)
        commit_info = commit_body.decode()
        print(f"COMMIT: {commit_id}")
        print(commit_info)
        
        commit_info = commit_info.split()
        tree_ind = commit_info.index('tree')
        tree_id = commit_info[tree_ind + 1]
        print(f"\nTREE: {tree_id}")
        draw_tree(repo_path, tree_id)
        if 'parent' not in commit_info:
            break
        parent_ind = commit_info.index('parent')
        commit_id = commit_info[parent_ind + 1]
        print('\n')

if len(sys.argv) <= 1:
    print(', '.join(listdir(branches_path)))
else:
    branch_name = sys.argv[1]
    branch_path = join(branches_path, branch_name)
    with open(branch_path, "r") as f:
        branch_id = f.read().strip()
    commit_story(repo_path, branch_id)    
