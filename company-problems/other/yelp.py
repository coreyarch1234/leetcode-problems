# 2d image array of colors problem where I had to return an array of the colors that appeared the most and if there were repeats, return them alphabetically.

import collections

def common_color(arr):
    max_count = 0
    color_dict = collections.defaultdict(int)
    for row in arr:
        for col in row:
            color_dict[col] += 1
            max_count = color_dict[col] if color_dict[col] > max_count else max_count
    colors = color_dict.items()
    ordered_colors = [name for name, count in colors if count == max_count]
    return sorted(ordered_colors)



input = [
    ['red', 'green', 'green'],
    ['blue', 'black', 'blue'],
    ['red', 'yellow', 'yellow']
] #  ['blue', 'green', 'red', 'yellow']

input2 = [
    ['red', 'green', 'green'],
    ['blue', 'black', 'blue'],
    ['red', 'yellow', 'yellow'],
    ['orange', 'red', 'orange']
] #  ['red']

input3 = [
    ['red', 'green', 'orange'],
] #  ['green', 'orange', 'red']

print common_color(input)
print common_color(input2)
print common_color(input3)
print common_color([])
