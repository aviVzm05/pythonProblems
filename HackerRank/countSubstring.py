def count_substring(string, sub_string):
    lenSub = len(sub_string)
    count = 0
    for i in range((len(string) - lenSub) + 1):
        if string[i:lenSub+i] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)