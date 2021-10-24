#can all the dogs be fed?

def validate_food(N,dog_portion,cat_portion,M):
    line = input()
    count = 0
    dog_count = 0
    for i in line:
        if i == 'C' and cat_portion > 0:
            cat_portion -= 1
            count += 1
        elif i == 'D' and dog_portion > 0:
            dog_portion -= 1
            cat_portion += M
            count += 1
            dog_count += 1
        elif (i == 'C' and cat_portion <= 0) or (i == 'D' and dog_portion <= 0):
            break
            
    if ((count == N) or dog_count == line.count('D')):
        return 'YES'
    else:
        return 'NO'



if  __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        N,D,C,M = list(map(int,input().split()))
        result = validate_food(N,D,C,M)
        print('Case #{}: {}'.format(i+1,result))