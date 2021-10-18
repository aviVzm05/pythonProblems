#Given the names and grades for each student in a class of N students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically
#and print each name on a new line.

#get the number of entries:

N = int(input())
nestedList = []

for _ in range(N):
    name = input().strip()
    score = float(input().strip())
    nestedList.append(list((name,score)))

# define a function to take each list  item and then return the score from it.
# sort will use this  as a key now. 

def takeScore(listItem):
    return listItem[1]

# sorted(nestedList,key=takeScore) sorted doesn't change the list, but returns sorted list.

nestedList.sort(key=takeScore) # this sorts  the  list  

# now, get the maximum value and check how many of these  maximum values are there in the list.

minScore = nestedList[0][1] # score from 1st element  of the list.

#flatten the entire nested list and see for, how many times max value occurs

flatList = [elm for list1 in nestedList for elm in list1]
times = flatList.count(minScore)

#so now, second lowest value... 
secondLowestScore = nestedList[times][1]  
# now, we can find how many times this score occurs from our above flatlist

# secondTimes = flatList.count(secondLowestScore)

# if the second lowest score occurs more than once, we need to print them in alphabetical order... 

#lets save the second lowest values to a new list

secondList = [list1 for list1 in nestedList if list1[1] == secondLowestScore]
secondList.sort()
for list1 in secondList:
    print(list1[0])

'''
Now, above solution works,  but the one that makes it ineresting is given in nestedListVersion1.py
'''