#https://www.hackerrank.com/challenges/py-check-subset/problem?h_r=next-challenge&h_v=zen

T = int(input())
for _ in range(T):
    countA = int(input())
    setA = set(map(int,input().split()))
    countB = int(input())
    setB = set(map(int,input().split()))
    print(setA.issubset(setB))