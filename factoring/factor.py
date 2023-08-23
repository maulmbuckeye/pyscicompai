import math
def factor(i: int):
    if i == 1:
        return {}
    for test_factor in range(2, int(math.sqrt(i))+1):
        if i % test_factor == 0:
            return add_values_in_dictionary({test_factor: 1}, factor(i//test_factor))
    return {i: 1}


def add_values_in_dictionary(a, b):
    return {key: a.get(key, 0) + b.get(key, 0) for key in set(a) | set(b)}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(200, 300):
        print(i, factor(i))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
