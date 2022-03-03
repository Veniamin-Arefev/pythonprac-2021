import textdistance


def dist(s1, s2, s3):
    return textdistance.levenshtein.distance(s1, s2)


str1, str2 = input().replace(' ', ''), input().replace(' ', '')

str3 = input().replace(' ', '')

result = dist(str1, str2, str3)
