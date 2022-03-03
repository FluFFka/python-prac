import textdistance
import multiprocessing as mp

def dist(s1, s2, t):
    if t == "L":
        return textdistance.levenshtein(s1, s2)
    elif t == "D":
        return textdistance.damerau_levenshtein(s1, s2)
    else:
        return -1

s1 = input()
s2 = input()
s3 = input()

pool = mp.Pool(1)
process = pool.apply_async(dist, (s1, s2, s3))
try:
    res = process.get(timeout=1)
except mp.context.TimeoutError:
    res = -1

