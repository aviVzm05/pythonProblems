#Let's learn about list comprehensions! 
# You are given three integers x,y and z representing the dimensions of a cuboid along with an 
# integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k  
# is not equal to n. Here, 0<= i; 0<=j; 0<=k . 
# Please use list comprehensions rather than multiple loops, as a learning exercise.

#  this works for alternate solution is in version1

def allPossible(x,y,z):
    allPossibleValues = []
    temp = []
    for i in range(x+1):
        for j in range(y + 1):
            for k in range(z + 1):
                temp.append(i)
                temp.append(j)
                temp.append(k)
                allPossibleValues.append(list(temp))
                temp.clear()

    return allPossibleValues





if __name__ == "__main__":
    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())
    n = int(input().strip())

    allPossibleValues = allPossible(x,y,z)
    answer = []
    for listVal in allPossibleValues:
        if (listVal[0] + listVal[1] + listVal[2]) != n:
            answer.append(listVal)
    else:
        print(answer)