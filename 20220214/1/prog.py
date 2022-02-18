from os import listdir
from os.path import join

repopath = join('..', '..')
branchpath = join(repopath, '.git', 'refs', 'heads')
print(', '.join(listdir(branchpath)))
