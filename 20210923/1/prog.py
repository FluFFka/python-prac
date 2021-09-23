n = int(input())
if n % 2 == 0 and n % 25 == 0:
    print('A+')
else:
    print('A-')
if n % 2 != 0 and n % 25 == 0:
    print('B+')
else:
    print('B-')
if n % 8 == 0:
    print('C+')
else:
    print('C-')

