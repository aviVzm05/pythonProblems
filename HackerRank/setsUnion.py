#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=false

n = int(input())
set1 = set(map(int,input().split()))
b =int(input())
set2 = set(map(int,input().split()))

#find the members who have atleast one subscription:

print(len(set1.union(set2)))
