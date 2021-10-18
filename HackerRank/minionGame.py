##Minion Game - https://www.hackerrank.com/challenges/the-minion-game/problem

vowels=tuple(("aeiou")) #Kevin
consonents = tuple(("bcdefghjklmnpqrstvwxyz"))  #Stuart

def minion_game(string):
    #loop over the entire string lenght and for each loop create a sub starting with the element for all lengths.
    subsCount = dict()
    string = string.lower()
    list1 = list(string)
    scoreV = 0
    scoreC = 0

    for index,l in enumerate(list1):
        count =1
        length = index + 1
        while length <= len(list1):
            substring = ''.join(list1[index:length])

            if substring in string:
                if substring in subsCount.keys():
                    subsCount[substring] += count
                else:
                    subsCount[substring] = count
            length += 1
        # list1.append(list1.pop(0))

    for key in subsCount.keys():
        if key[0:1] in vowels:
            scoreV += subsCount[key]
        else:
            scoreC += subsCount[key]

    if scoreV > scoreC:
        print('Kevin {}'.format(scoreV))
    elif scoreC > scoreV:
        print('Stuart {}'.format(scoreC))
    else:
        print('Draw')

    return

if __name__ == "__main__":
    s = input().strip().lower()
    minion_game(s)