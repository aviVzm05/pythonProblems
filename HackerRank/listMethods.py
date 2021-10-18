N = int(input())

listVar = list()
listVar1 = list()

for _ in range(N):
    command,*variables = input().split()

    ### alternate solution is to use eval method.
    if command != "print":
        command += "("+','.join(variables)+")"
        eval("listVar1."+command)
    else:
        print(listVar1)

    #convert the values to int first... 
    variables = list(map(int,variables))
    if command == 'insert':
        listVar.insert(variables[0],variables[1])
    elif command == 'print':
        print(listVar)
    elif command == 'remove':
        listVar.remove(variables[0])
    elif command == 'append':
        listVar.append(variables[0])
    elif command == 'sort':
        listVar.sort()
    elif command == 'pop':
        listVar.pop()
    elif command == 'reverse':
        listVar.reverse()

