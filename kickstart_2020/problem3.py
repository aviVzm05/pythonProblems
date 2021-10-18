def main():
    test_cases = int(input())
    for T in range(test_cases):
        dict = {}
        dataIn = input()
        for l in range(len(dataIn)):
            counter = 1
            if dataIn[l] in dict:
                counter = dict[dataIn[l]]
                counter += 1
                dict[dataIn[l]] = counter
            else:
                dict[dataIn[l]] = counter
        #sort based on ley values...
        sorted_list_keys = sorted(dict, key=dict.get, reverse=True)
        max = dict[sorted_list_keys[0]]
        key_max = sorted_list_keys[0]
        #skip max - 1st record from the list
        for i in range(1,len(sorted_list_keys)):
            key = sorted_list_keys[i]
            if max == dict[key]:
                if key < key_max:
                    key_max = key
        print(key_max)
            
main();