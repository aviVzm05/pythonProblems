#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from itertools import combinations

# learning is that, we need to sort the string first and then do the combinations... to get the 
# data in sorted order... as combinations use the position in list for coming up with possible values.

S,K = input().split()
list1 = sorted(list(S))
K = int(K)
for i in range(1,K+1):
    list2 = (combinations(list1,i))
    for string in list2:
        print(("").join(string))