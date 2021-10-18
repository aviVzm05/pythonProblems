#Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up

#The first line contains n. 
#The second line contains an array A[]  of n integers each separated by a space.

numberOfEntries = int(input())
# listOfNumbers = input().split() # converts the values taken into a list... but,they are in str.. not int.

# this works  -  we are running a int funciton on each list element. 
# listOfNumbers = map(int,input().split())
# print(list(listOfNumbers))

listVal = input().split() # now, this creates a string list... 
newlist = [int(x) for x in listVal]
# print(newlist)
newlist.sort(reverse=True)

# have to remove duplicates as there can be more than 1 top score.. and above logic fails in that case
dupsMax = newlist.count(newlist[0])
runnerUp = newlist[0 + dupsMax]
print(runnerUp)

print(sorted(set(newlist))[-2])