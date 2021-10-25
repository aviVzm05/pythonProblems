#https://www.hackerrank.com/challenges/py-set-add/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

N = int(input().strip())
set1 = set()
for i in range(N):
    set1.add(input().strip())
print(len(set1))
set1.add('avinash')
print(set1)