#https://www.hackerrank.com/challenges/no-idea/problem?h_r=next-challenge&h_v=zen

n,m = map(int,input().split())
arrayIn = list(map(int,input().split()))
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))

happiness = 0

for i in arrayIn:
    if i in setA:
        happiness += 1
    elif i in setB:
        happiness -= 1
    else:
        happiness += 0

print(happiness)