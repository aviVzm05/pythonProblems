#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a 
# list of students. Print the average of the marks array for the student name provided,
# showing 2 places after the decimal.

if __name__ == "__main__":
    dictElement = dict()
    n = int(input())
    for _ in range(n):
        name,*line = input().split()
        # line is a list of scores provided... 
        scores = list(map(float,line))
        dictElement[name] = scores
    
    nameToPrint = input()
    score1, score2, score3 = dictElement[nameToPrint]
    averageScore = (score1+score2+score3)/3
    print("{:.2f}".format(averageScore))