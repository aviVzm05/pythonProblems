#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=false

from itertools import product

if __name__ == '__main__':
    listA = list(map(int,input().split()))
    listB = list(map(int,input().split()))
    list1 = [(x,y) for x in listA for y in listB]
    print(*sorted(list1))
    print(sorted(list(product(listA,listB))))
            
