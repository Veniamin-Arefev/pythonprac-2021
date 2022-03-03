import textdistance


def dist(s1, s2, s3):
    if s3 == "L":
        return textdistance.levenshtein.distance(s1, s2)
    elif s3 == "D":
        return textdistance.damerau_levenshtein.distance(s1, s2)
    else:
        return -1


str1, str2 = input().replace(' ', ''), input().replace(' ', '')

str3 = input().replace(' ', '')

result = dist(str1, str2, str3)
