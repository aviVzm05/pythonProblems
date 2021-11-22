#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from  itertools import permutations,combinations,product
from typing import Match, Protocol

def function(i):
    return (i**2)

def function1(tupl1):
    return sum(tupl1)%M

if __name__ == "__main__":
    global M
    K, M = list(map(int,input().split()))
    dict1 = dict()
    for i in range(K):
        number,*list1 = map(int,input().split())
        list2 = list(map(function,list1))
        dict1[i] = list2
    
    # print(list(combinations(max,K)))
    # print(sum(sorted(list(combinations(max,K)),reverse=True,key=function1)[0])%M)
    print(sum(sorted(list(product(*dict1.values())),reverse=True,key=function1)[0])%M)