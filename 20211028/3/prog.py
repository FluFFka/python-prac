import itertools
print(', '.join(sorted(set(filter(lambda x: x.count("TOR") == 2, [''.join(i) for i in itertools.product("TOR", repeat=int(input()))])))))
