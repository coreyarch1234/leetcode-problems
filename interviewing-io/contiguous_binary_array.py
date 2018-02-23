input_arr_one = [0,1,1,0,1,1,1,0,0]
input_arr_two = [1, 0, 1, 1, 0]
def longest_arr(arr):
    if arr == []:
        return 0
    curr_arr = []
    max_arr = []
    max_count = 0
    max_dict = {
        "0": 0,
        "1": 0
    }
    iteration_dict = {}

    for num in arr:
        print "num: ",num
        if num == 0:
            max_dict["0"] += 1
            curr_arr.append(0)
        else:
            max_dict["1"] += 1
            curr_arr.append(1)

        if max_dict["0"] == max_dict["1"]:
            print "they are equal"
            print "0 count: ",max_dict["0"]
            print "1 count: ",max_dict["1"]
            print
            if len(curr_arr) > len(max_arr):
                max_arr = curr_arr[:]
    max_count = len(max_arr)

    if len(arr[1:]) > max_count:
        return max(max_count, longest_arr(arr[1:]))
    else:
        return max_count

print longest_arr(input_arr_one)

# given an int array
# Consists of 0 and 1s
# find the longest contiguous subarray where number of 0 and 1 is equal

# [0,1,1,0]
# [0, 1, 1, 0, 1]

# 0s: 1 + 1
# 1s: 1 + 1 + 1
# d:    1, 0,-1, 0,-1
# left: 4, 3, 2, 1, 0

# [1, 0, 1, 1, 0]
# diff = x - y, x = num 0, y = num 1
# 0s: 1
# 1s: 1 + 1 + 1
# d: -1 0 -1 -2 -1
#     4 3  2  1  0
# 1, 0,-1,-2
# left: 4, 3, 2, 1

# need : arr to hold subarray

# [1,1,1,1,1]
#d:-1 -2 -3 4 5
#l: 5 4 3 2 1

# [0, 1, 1, 0, 1] 4
# [1, 0, 1, 1, 0] 4
# def find_arr_diff(arr):
#     diff = 0
#     num_zeroes = 0
#     num_ones = 0
#     left = len(arr)
#     count = 0
#     for index, num in enumerate(arr):
#         if num == 0:
#             num_zeroes += 1
#         else:
#             num_ones += 1
#         # if diff + left < 0:
#         #     return index
#         diff = num_zeroes - num_ones
#         left -= 1
#         print "zeroes: ",num_zeroes
#         print "ones: ",num_ones
#         print "diff: ",diff
#         print "left: ",left
#         print
#         if diff + left < 0:
#             return index
#
#
# print find_arr_diff([0, 1, 1, 0, 1])





#
# Your previous Plain Text content is preserved below:
#
# Welcome to your interviewing.io interview.
#
# Once you and your partner have joined, a voice call will start automatically.
#
# Use the language dropdown near the top right to select the language you would like to use.
#
# You can run code by hitting the 'Run' button near the top left.
#
# Enjoy your interview!
