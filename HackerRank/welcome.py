#print a welcome screen.
def printWelcome(y,x):
    #y is length and x is width
    for i in range(y):
        if i+1 == ((y+1)/2):
            print("WELCOME".center(x,'-'))
        elif i+1 < ((y+1)/2):
            string = ".|."*((i*2 + 1))
            print(string.center(x,"-"))
        else:
            string = ".|."*(((y-(i+1))*2) +1)
            print(string.center(x,"-"))

if __name__ == "__main__":
    datain = input().split() # this is a list now
    convertToInt = list(map(int,datain)) # convert to int
    y,x = convertToInt
    printWelcome(y,x)

## below code is an alternate and amazing code that works as well

# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))