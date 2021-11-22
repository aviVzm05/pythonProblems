#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=false

from itertools import combinations

lengthOfInput = int(input())
list1 = input().split()
index = int(input())

listOfPossibilities = combinations(list1,index)
# print(list(listOfPossibilities))

total, count = (0,0)
for tuple1 in listOfPossibilities:
    total = total + 1
    if tuple1.count('a') > 0:
        count += 1

print('{:.3f}'.format(count/total))