from collections import Counter
import re

n = int(input())
con = Counter()
try:
    while a := input():
        con += Counter(filter(lambda x: len(x) == n and str.isalnum, re.split(r'\W+', a.lower())))
except:
    pass
if con:
    print(*[key for key, val in con.items() if len(key) == n and val == max(con.values())])
