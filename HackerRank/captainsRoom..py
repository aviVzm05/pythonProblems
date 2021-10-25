#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=false
K = int(input())
roomEntries = input().split()
roomEntriesSet = set(roomEntries)

for i in roomEntriesSet:
    roomEntries.remove(i)
    if i not in roomEntries:
        print(i)
        break
        