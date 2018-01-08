# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
# 
#
# def containsNearbyDuplicate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     nums_dup = {}
#     for index, num in enumerate(nums):
#         if num in nums_dup:
#             nums_dup[num].append(index)
#             index_dup_arr = nums_dup[num]
#             for i in range(len(index_dup_arr) - 1):
#                 if abs(index - index_dup_arr[i]) <= k:
#                     return True
#         else:
#             nums_dup[num] = [index]
#     return False

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    nums_dup = {}
    for index, num in enumerate(nums):
        if num in nums_dup:
            if abs(index - nums_dup[num]) <= k:
                return True
            else:
                nums_dup[num] = index
        else:
            nums_dup[num] = index
    return False


print containsNearbyDuplicate([1, 0, 1, 1], 1)
