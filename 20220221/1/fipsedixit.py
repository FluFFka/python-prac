from ipsedixit import Generator
import sys
from ipsedixit import parse_args

i = 1
pos = -1
pos_find = False
while i < len(sys.argv):
    if sys.argv[i][0] == '-':
        if i + 1 < len(sys.argv):
            if sys.argv[i + 1][0] != '-':
                i += 1
    else:
        if not pos_find:
            pos_find = True
        else:
            pos = i
            break
    i += 1
if pos != -1:
    if sys.argv[pos] in ('caesar', 'tacitus'):
        text = sys.argv[pos]
    else:
        with open(sys.argv[pos], 'r') as f:
            text = f.read()
    sys.argv.pop(pos)
else:
    text = False
args = parse_args()
if text:
    generator = Generator(text)
else:
    generator = Generator()
print('\n\n'.join(generator.paragraphs(args.num, args.min, args.max)))
