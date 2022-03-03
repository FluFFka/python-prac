import textdistance

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

res = dist(s1, s2, s3)
