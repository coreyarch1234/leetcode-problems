# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse_list(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        data_queue = []
        curr = head
        while curr is not None:
            data_queue.append(curr.val)
            curr = curr.next
        curr = self.reverse_list(head)
        data_queue = data_queue[::-1]
        while curr is not None:
            if data_queue.pop() != curr.val:
                return False
            curr = curr.next
        return True
