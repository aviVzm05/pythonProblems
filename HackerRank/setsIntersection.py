#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

n = int(input())
set1 = set(map(int,input().split()))
b = int(input())
set2 = set(map(int,input().split()))

print(len(set1 & set2)) # & or .intersection can be used...