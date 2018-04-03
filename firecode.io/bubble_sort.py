# Write a function that takes in a list of ints and uses
# the Bubble Sort algorithm to sort the list 'in place' in ascending order. The method should return the same, in-place sorted list.
# Note: Bubble sort is one of the most inefficient ways to sort a large list of integers. Nevertheless, it is an interview favorite.
# Bubble sort has a time complexity of O(n2). However, if the
# sample size is small, bubble sort provides a simple implementation of a classic sorting algorithm.
#
# Examples:
# bubble_sort([5, 4, 3]) -> [3, 4, 5]
#
# bubble_sort([3]) -> [3]
#
# bubble_sort([]) -> []
#
# [] -> [Empty] List
#

def check_sort(a_list):
    return a_list == sorted(a_list)

def bubble_sort(a_list):
    # have 2 pointers
    # check if list still unsorted
    # reset check when you bubble next largest to end
    # end when you loop through list and check remains valid until end
    if a_list <= 1:
        return a_list

    first_pointer = 0
    second_pointer = 1
    sort_count = 1
    a_list_len = len(a_list)

    while check_sort(a_list) is False:
        print 'a_list: ',a_list
        #unordered
        if a_list[second_pointer] <= a_list[first_pointer]:
            a_list[second_pointer], a_list[first_pointer] = a_list[first_pointer], a_list[second_pointer] #swap
            first_pointer += 1
            second_pointer += 1
            if second_pointer > a_list_len - 1:
                first_pointer = 0
                second_pointer = 1
            print 'swapped: ',a_list
        else:
            first_pointer += 1
            second_pointer += 1
            if second_pointer > a_list_len - 1:
                first_pointer = 0
                second_pointer = 1

    print 'ordered: ',a_list
    return a_list


# good solution not mine
# def bubble_sort(a_list):
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         for i in range(len(a_list)-1):
#             if a_list[i] > a_list[i+1]:
#                 a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
#                 is_sorted = False
#     return a_list












# a_list = [5, 4, 3]
a_list = [1, 4, 5, 0, 2]
print bubble_sort(a_list)
