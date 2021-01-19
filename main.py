import sys
from collections import OrderedDict
import time


def find_unique(array: list) -> list:
    result_array = []
    for word in array:
        for letter in word:
            if list(word).count(letter) == 1:
                result_array.append(letter)
                break
    return result_array


def find_unique2(array: list) -> list:
    result_dict = OrderedDict()
    for word in array:
        hash_dict = OrderedDict()
        for letter in word:
            if letter not in hash_dict.keys():
                hash_dict.update({letter: 1})
            else:
                hash_dict[letter] += 1
        for key, val in hash_dict.items():
            if val == 1:
                if key not in result_dict.keys():
                    result_dict.update({key: 1})
                else:
                    result_dict[key] += 1
                break
    for res_key, res_val in result_dict.items():
        if res_val == 1:
            return res_key


if __name__ == '__main__':
    data = sys.stdin.read().replace(".", " ").replace("-", " ")
    splited = data.split()
    start_time = time.time()
    part_res = find_unique(splited)
    result = find_unique(["".join(part_res)])
    print("Result of finding unique is -> '{}'".format(result[0]))
    print("Time to execute var1 == ", time.time() - start_time)
    start_time = time.time()
    result = find_unique2(splited)
    print("Result of finding unique is -> '{}'".format(result[0]))
    print("Time to execute var2 == ", time.time() - start_time)
