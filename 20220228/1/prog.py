import textdistance

def dist(s1, s2):
    return textdistance.levenshtein(s1, s2)

s1 = input()
s2 = input()
s3 = input()

res = dist(s1, s2)
