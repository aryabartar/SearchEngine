import math
import numpy as np

dict = {"MahSa": {3: [2, 4, 7, 9], 4: [6, 9, 13]}, "Akbar": {14: [3, 4, 5]}, "as": {14: [6, 7, 8]}}


def get_lengths(dict, token):
    return len(dict.get(token, {}).keys())


def get_len_char(dict, token, docid):
    key = dict.get(token, {})
    result = key.get(docid, [])
    return len(result)


# final = np.zeros((1731, 542879))
final = [[0] * 542879] * 1731


def calculate():
    for i, key in enumerate(DATA_DICT.keys()):
        for j in range(0, 1731):
            w = (math.log10(1 + get_len_char(DATA_DICT, key, j))) * (
                math.log10(1731 / get_lengths(DATA_DICT, key)))
            final[j][i] = w


def print_nonzero(row):
    for i in row:
        if i != 0:
            print(i)


calculate()
print_nonzero(final[4])

