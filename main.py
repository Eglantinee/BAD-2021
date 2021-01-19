import sys


def find_unique(array: list) -> list:
    result_array = []
    for word in array:
        for letter in word:
            if list(word).count(letter) == 1:
                result_array.append(letter)
                break
    return result_array


if __name__ == '__main__':
    data = sys.stdin.read().replace(".", " ").replace("-", " ")
    splited = data.split()
    part_res = find_unique(splited)
    result = find_unique(["".join(part_res)])
    print("Resul of finding unique is -> '{}'".format(result[0]))
