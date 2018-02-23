# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]

print findKthLargest([3,2,1,5,6,4], 2)
