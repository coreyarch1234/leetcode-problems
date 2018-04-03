# Reverse a singly linked list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        previous_node = head
        next_node = previous_node.next
        temp_node = next_node.next

        if temp_node is None:
            previous_node.next = None
            next_node.next = previous_node
            return next_node

        if previous_node == head:
                previous_node.next = None

        while temp_node is not None:
            next_node.next = previous_node
            previous_node = next_node
            next_node = temp_node
            temp_node = next_node.next

        next_node.next = previous_node
        return next_node

        
