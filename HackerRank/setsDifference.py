#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# find out the students that are only subscribed to English newsaper
n = int(input())
english = set(map(int,input().split()))
b = int(input())
social = set(map(int,input().split()))

print(len(english - social)) # or it can be mentioned as english.difference(social)