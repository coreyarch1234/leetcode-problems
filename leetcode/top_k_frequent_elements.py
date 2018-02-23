# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


import collections
# O(Nlog(N)) Runtime
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    frequent_dict = collections.Counter()
    for num in nums:
        frequent_dict[num] += 1

    most_common = frequent_dict.most_common()
    most_common_arr = []
    index = 0
    while index < k:
        most_common_arr.append(most_common[index][0])
        index += 1
    return most_common_arr
