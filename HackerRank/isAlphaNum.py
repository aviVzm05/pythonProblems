# print true if any charecter if alphabetic/numeric/lower case/upper case

def print_Type(s):
    validationQ = ["isalnum","isalpha","isdigit","islower","isupper"]
    validationA = dict()
    temp = []
    for x in s:
        for v in validationQ:
            temp.append(eval("x."+v+"()"))
        validationA[x] = temp.copy()
        temp.clear()
    
    for index,val in enumerate(validationQ):
        count = 0
        for key in validationA.keys():
            if validationA[key][index]:
                count += 1
                break
        if count > 0:
            print(True)
        else:
            print(False)
        count = 0

#alternate solution would be to use any function -
#This returns true if any item in the iterable is true  for the function

if __name__ == "__main__":
    s = input()
    # print_Type(s)
    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print(any(method(c) for c in s))