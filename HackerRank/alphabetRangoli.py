# print alphabet rangoli....

def print_rangoli(size):
    small_letters = tuple(map(chr, range(ord('a'), ord('z')+1)))
    listOfVariables = []
    outputToPrint = []

    for i in range(size):
        listOfVariables.append(small_letters[i])
        if i !=0:
            listOfVariables.insert(0,small_letters[i])
    
    lengthOfOutput = len("-".join(listOfVariables))

    while len(listOfVariables) > 0:
        outputToPrint.insert(0,"-".join(listOfVariables).center(lengthOfOutput,"-"))
        toRemove = int((len(listOfVariables)+1)/2)-1
        listOfVariables.pop(toRemove)
        if len(listOfVariables) > 1:
            listOfVariables.pop(toRemove)
    
    if len(outputToPrint) > 1:
        print("\n".join(outputToPrint)+"\n"+"\n".join(outputToPrint[len(outputToPrint)-2::-1]))
    else:
        print("\n".join(outputToPrint))

if __name__ == "__main__":
    size = int(input().strip())
    print_rangoli(size)
