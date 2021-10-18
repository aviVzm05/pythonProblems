# x,y,z,n = int(input()),int(input()),int(input()),int(input())
x,y,z,n = (int(input()) for _ in range(4)) # we are unpacking a tuple here.
# Also, 
# _ is used to signify that even though something is being returned, we don't plan to use that variable any where.


'''
Entire logic below works okay... but there is an even simple  solution... 
'''

print([list((i,j,k)) for i in range(x+1) for j  in range(y+1) for k in range(z + 1) if (i + j + k != n) ])

listValue = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z + 1):
            if i + j + k != n:
                listValue.append(list((i,j,k)))

print(listValue)
