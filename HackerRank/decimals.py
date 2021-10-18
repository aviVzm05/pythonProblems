# print decimal, octal, hexadecimal values.... 
number = int(input().strip())

for i in range(1,number+1):
    length = len(bin(number)[2:])
    print('{} {} {} {}'.format(str(i).rjust(length),oct(i)[2:].rjust(length),hex(i)[2:].upper().rjust(length),bin(i)[2:].rjust(length)))