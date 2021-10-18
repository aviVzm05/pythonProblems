def swap_case(string):
    stringList = [x.swapcase() for x in string]
    return ''.join(stringList)


if __name__ == "__main__":
    stringInput = input()
    swappedString = swap_case(stringInput)
    print(swappedString)