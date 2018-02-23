# 3Sum
# https://leetcode.com/problems/3sum/description/
# 3Sum
# Difficulty:Medium
#
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    solution = []
    nums.sort()
    nums_len = len(nums)

    p_1 = 0
    p_2 = p_1 + 1
    p_3 = nums_len - 1
    finished = False

    while finished == False:
        if p_2 + 1 == p_3:
            p_1, p_2, p_3 = p_1 + 1, p_2 + 1, nums_len - 1
            continue
        if p_2 == p_1 + 1 and p_3 == p_2 + 1:
            finished = True
            continue
        potential = nums[p_1] + nums[p_2] + nums[p_3]
        if potential == 0:
            solution.append([nums[p_1], nums[p_2], nums[p_3]])
            p_1, p_2, p_3 = p_1 + 1, p_2 + 1, nums_len - 1
            continue
        elif potential < 0: # too low
            p_2 += 1
        elif potential > 0:
            p_3 -= 1
    return solution

print threeSum([-1,0,1,2,-1,-4])
