def split_and_join(line):
    stringSplit = line.split(" ")
    print(stringSplit)
    return '-'.join(stringSplit)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)