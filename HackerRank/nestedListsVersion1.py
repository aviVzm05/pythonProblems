marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

marksheet = [[input(), float(input())] for _ in range(int(input()))]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1] 
# note that set removes dulicates... so we get the marks individually...
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))