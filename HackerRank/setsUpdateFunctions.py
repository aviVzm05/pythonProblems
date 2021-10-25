#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

N = int(input().strip())
A = set(map(int,input().strip().split()))
number = int(input())

for i in range(number):
    function, length = input().strip().split()
    set2 = set(map(int,input().strip().split()))
    eval('A.'+function+'(set2)')
    del set2

print(sum(A))