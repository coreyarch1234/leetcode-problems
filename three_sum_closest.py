# https://leetcode.com/problems/3sum-closest/description/
#
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    close_sum = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            if current_sum == target:
                return current_sum
            if abs(current_sum - target) < abs(close_sum - target):
                close_sum = current_sum
            if current_sum < target:
                j += 1
            elif current_sum > target:
                k -= 1
    return close_sum
