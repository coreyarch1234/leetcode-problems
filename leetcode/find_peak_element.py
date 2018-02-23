# https://leetcode.com/problems/find-peak-element/description/
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 2:
        return nums.index(max(nums))

    pointer_zero, pointer_one = 0, 1

    while pointer_one < len(nums) - 1:
        print pointer_one
        if nums[pointer_zero] < nums[pointer_one]:
            # print "yes"
            if nums[pointer_one + 1] < nums[pointer_one]:
                # print "yes more"
                return pointer_one
            else:
                pointer_zero, pointer_one = pointer_one, pointer_one + 1
        else:
            pointer_zero, pointer_one = pointer_one, pointer_one + 1
    return nums.index(max(nums))

def findPeakElementBetter(nums):
    # only need to check ahead
    if len(nums) == 1:
        return 0
    current = nums[0]
    for index in range(len(nums) - 1):
        if current > nums[index + 1]:
            return index
        current = nums[index + 1]
    return len(nums) - 1

print findPeakElementBetter([1,2,3,1])
