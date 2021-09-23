n = int(input())
col = n
while col < n + 3:
    row = n
    while row < n + 3:
        num_sum = 0
        check = abs(col*row)
        while check:
            num_sum += check % 10
            check //= 10
        print(col, '*', row, '=', col*row if num_sum != 6 else ":=)", end=" ", sep="")
        row += 1
    print()
    col += 1
