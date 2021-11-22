#https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=false

from itertools import groupby

stringInput = input()

iterlist = groupby(stringInput)

list1 = []

for key,groupIterList in iterlist:
    length = len(list(groupIterList))
    list1.append(tuple((length,int(key))))

print(*list1)