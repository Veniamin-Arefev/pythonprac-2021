import textdistance


def dist(s1, s2):
    return textdistance.levenshtein.distance(s1, s2)
