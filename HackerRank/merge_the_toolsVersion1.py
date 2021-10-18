#https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen
#create subsequence of numbers...

from typing import final


def merge_the_tools(string, k):
    # your code goes here
    # number_of_substrings = int(len(string)/k)aaa
    for i in range(0,len(string),k):
        uniq = ''
        for c in string[i : i+k]:
            if (c not in uniq):
                uniq+=c
        print(uniq)


    return

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)