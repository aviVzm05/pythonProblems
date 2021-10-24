#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=false

def average(array):
        array1 = set(array)
        val1 = sum(array)/len(array)
        return f"{val1:0.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)