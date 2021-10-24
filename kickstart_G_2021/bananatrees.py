def minimum_trees(N,K,trees_list):
    #total number of bananas in the trees given should not be more than capacity or less...
    for index,elm in enumerate(trees_list):
        base = trees_list[0]
        for j in range(1,len(trees_list)):
            sum = base
            sum +=  trees_list[j]
            if sum == K:
                return 2
        trees_list.append(trees_list.pop(0)) # we have shifted the elements by 1.


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        N,K = list(map(int,input().split()))
        trees_list = list(map(int,input().split()))
        result = minimum_trees(N,K,trees_list)
        print('yep it worked.')