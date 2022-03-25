import re


def spaceCount(str):
    brCount = 0
    count = 0
    spaceStr = re.match('^([\n\s\r]+)\w?', str)
    if spaceStr is not None:
        brCount = spaceStr.group().count('\t')
        count = spaceStr.group().count(' ')
    count = (brCount * 4) + count
    return count


def findAll(sub, s):
    indexList = []
    index = s.find(sub)
    while index != -1:
        indexList.append(index)
        index = s.find(sub, index + 1)
    if len(indexList) > 0:
        return indexList
    else:
        return -1


def minDistance(w1, w2):
    m, n = len(w1), len(w2)
    if m == 0:
        return m
    if n == 0:
        return n
    step = [[0] * (n+1)for _ in range(m+1)]
    for i in range(1, m+1):step[i][0] = i
    for j in range(1, n+1):step[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if w1[i-1] == w2[j-1] :
                diff = 0
            else:diff = 1
            step[i][j] = min(step[i-1][j-1], min(step[i-1][j], step[i][j-1])) + diff
    return step[m][n]