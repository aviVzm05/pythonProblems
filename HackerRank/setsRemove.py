#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

elements_in_set = int(input().strip())
set1 = set(map(int,input().split()))
functionsToExecute = int(input())

for f in range(functionsToExecute):
    function = '{0}({1})'.format(*tuple(input().split())+ tuple(' '))
    eval('set1.'+function)
print(sum(set1))