import sys
import ast
import textdistance
import difflib

if len(sys.argv) >= 3:
    prog1_name = sys.argv[1]
    prog2_name = sys.argv[2]

with open(prog1_name) as f:
    prog1 = f.read()
with open(prog2_name) as f:
    prog2 = f.read()

prog1 = ast.unparse(ast.parse(prog1))
prog2 = ast.unparse(ast.parse(prog2))

def visit(node):
    res = ''
    for inner in ast.iter_child_nodes(node):
        res += type(node).__name__[0] + '/' + visit(inner)
    return res + '../'

res1 = visit(ast.parse(prog1))
res2 = visit(ast.parse(prog2))

copy_f = textdistance.damerau_levenshtein.normalized_distance(res1, res2)
if copy_f <= 0.1:
    print(difflib.HtmlDiff().make_file(prog1.split('\n'), prog2.split('\n')))
else:
    print(copy_f)
