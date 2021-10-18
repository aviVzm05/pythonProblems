#https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen
#create subsequence of numbers...

from typing import final


def merge_the_tools(string, k):
    # your code goes here
    # number_of_substrings = int(len(string)/k)
    substrings = []
    dict1 = dict()
    finalList = []
    for i in range(0,len(string),k):
        substrings.append(string[i:(i+k)])
    
    for substring in substrings:
        print('{} this is the sub'.format(substring))
        dict1.clear()
        list1 = list(substring)
        for i in list1:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
        list2 = [x for x in dict1.keys()]
        string1 = ''.join(list2)
        finalList.append(string1)
    print('\n'.join(finalList))


    return

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)