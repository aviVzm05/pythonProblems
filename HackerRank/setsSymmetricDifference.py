#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=false

numberSet1 = int(input())
set1 = set(map(int,input().split()))
nummberSet2 = int(input())
set2 = set(map(int,input().split()))

print('\n'.join(map(str,sorted(set1.symmetric_difference(set2)))))
# print(type(sorted(set1.symmetric_difference(set2))))
# print('\n'.join(sorted(list(set1.symmetric_difference(set2)))))
# print(sorted(list(set1.symmetric_difference(set2))))