# Task
# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // . 
# The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.


def printDivision(a,b):
    print(a//b)
    print(a/b)
    return

if __name__ == '__main__':
    first_num = int(input().strip())
    second_num = int(input().strip())
    printDivision(first_num,second_num)