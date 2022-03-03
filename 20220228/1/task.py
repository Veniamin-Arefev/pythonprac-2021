import textdistance


def dist(s1, s2):
    return textdistance.levenshtein.distance(s1, s2)


str1, str2 = input().replace(' ', ''), input().replace(' ', '')

result = dist(str1, str2)
