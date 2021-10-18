##Minion Game - https://www.hackerrank.com/challenges/the-minion-game/problem

vowels=tuple(("aeiou")) #Kevin
consonents = tuple(("bcdefghjklmnpqrstvwxyz"))  #Stuart

def minion_game(string):
    string = string.lower()
    scoreV = scoreC = 0

    for index in range(len(string)):
        if string[index] in vowels:
            scoreV += len(string) - index
        else:
            scoreC += len(string) - index


    if scoreV > scoreC:
        print('Kevin {}'.format(scoreV))
    elif scoreC > scoreV:
        print('Stuart {}'.format(scoreC))
    else:
        print('Draw')

    return

if __name__ == '__main__':
    s = input()
    minion_game(s)