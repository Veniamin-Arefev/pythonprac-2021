import textdistance
import multiprocessing


def dist(s1, s2, s3):
    if s3 == "L":
        return textdistance.levenshtein.distance(s1, s2)
    elif s3 == "D":
        return textdistance.damerau_levenshtein.distance(s1, s2)
    else:
        return -1


str1, str2 = input().replace(' ', ''), input().replace(' ', '')

str3 = input().replace(' ', '')

my_pool = multiprocessing.pool.Pool(1)

process = my_pool.apply_async(dist, args=((str1, str2, str3)))

result = process.get()

print(result)
