a, b = eval(input())
print([j for j in range(a, b) if j > 1 and all([j%i for i in range(2, int(j**0.5)+1)])])
