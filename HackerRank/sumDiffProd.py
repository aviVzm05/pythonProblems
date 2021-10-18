# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def printInfo(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    return


if __name__ == '__main__':
    first_number = int(input().strip())
    second_number = int(input().strip())
    printInfo(first_number,second_number)