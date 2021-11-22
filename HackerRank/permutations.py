#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=false&h_r=next-challenge&h_v=zen
from itertools import permutations

S,K = input().split()
k = int(K)
list1 = sorted(list(permutations(S,k)))
for string in list1:
    print(("").join(string))