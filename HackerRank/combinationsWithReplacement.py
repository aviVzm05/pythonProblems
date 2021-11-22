#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from itertools import combinations_with_replacement

S,K = input().split()
K = int(K)
list1 =  sorted(list(S))

for string in combinations_with_replacement(list1,K):
    print(("").join(string))