#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#symmmetric difference is essentially finding out number of entries that are in either of the sets, but not in both.

n = int(input())
english = set(map(int,input().split()))
b = int(input())
social = set(map(int,input().split()))
print(len(english.symmetric_difference(social)))
print(len(english.union(social) - english.intersection(social)))

#both above are the same...