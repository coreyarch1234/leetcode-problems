# https://www.getpy.com/hashtable/challenge?find-the-singleton
#
# In an array a numbers, each number appears twice except one number that appears only once. Find the number that appears only once.
#
# This can be done in O(1) space and O(n) time.

# TIME - 9 MIN
def solution(numbers): # RUNTIME - O(N) AND SPACE COMPLEXITY OF O(1)
    # Type your solution here

    number_dict = {}
    num_array = []
    num_sum = sum(numbers) # O(N)
    for num in numbers: # O(N)
        if num in number_dict:
            num_array.append(2 * num) # O(1)
        else:
            number_dict[num] = 1
    return num_sum - sum(num_array) # O(1)
