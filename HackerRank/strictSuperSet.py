#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

setA = set(input().split())
N = int(input())
isStrict = True

for _ in range(N):
    setB = set(input().split())
    if setA.issuperset(setB):
        if len(setA.difference(setB)) == 0:
            isStrict = False
    else:
        isStrict = False
print(isStrict)