# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following - 12345....n
# Note that "" represents the consecutive values in between.

def printNumbers(n):
    consecNumber = ''
    for i in range(1,n+1):
        consecNumber = consecNumber + str(i)
    return consecNumber

if __name__ == "__main__":
    number = int(input().strip())
    # print(printNumbers(number))
    for i in range(1,number+1):
        print(i,end='')