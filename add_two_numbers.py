# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #for the first linked List
        first_sum = 0
        first_index = 0
        current_one = l1
        while current_one.next is not None:
            first_sum += current_one.val * pow(10, first_index)
            first_index += 1

        #for the second linked List
        second_sum = 0
        second_index = 0
        current_two = l2
        while current_two.next is not None:
            second_sum += current_two.val * pow(10, second_index)
            second_index += 1

        return first_sum + second_sum
