# https://leetcode.com/problems/contains-duplicate/description/
#
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


def containsDuplicate(nums):
    if len(nums) <= 1:
        return False
    without_dup = list(set(nums))
    return len(nums) != len(without_dup)
