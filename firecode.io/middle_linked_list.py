# Faster solution using 2 pointers
#
# What we'll do is setup two pointers, one that will traverse the linked list one node at a time, and the other pointer will traverse two nodes at a time. This way when the faster pointer reaches the end of the linked list, the slower pointer will be halfway there because it was only moving one node at time while the faster one was moving two nodes at a time. This allows you to find the middle node of a linked list with only one pass, instead of passing through the whole linked list once, and then again to find the middle element.

# best solution:
# setup pointers to both start
# at the head of the linked list
fastPointer = head
slowPointer = head

# loop through the linked list
# when fastPointer reaches the end of the list
# then slowPointer will be at the middle node
while fastPointer.next != None and fastPointer.next.next != None:
  fastPointer = fastPointer.next.next
  slowPointer = slowPointer.next

# slowPointer is now at the middle node in the linked list
print slowPointer.data


#
# # same runtime, but 2 for loops
# class SinglyLinkedList:
#     #constructor
#     def __init__(self):
#         self.head = None
#
#     #method for setting the head of the Linked List
#     def setHead(self,head):
#         self.head = head
#
#     # method to take length and determine middle and return that index
#     # ex. length = 1, 0, middle = 0, return 0
#     # ex. length = 2, 0, 1, middle = 0, return 0
#     # ex. length = 3, 0, 1, 2, middle = 1, return 1,
#     # keep going until end of LL and when done, run through LL again and return node at that index
#     def find_middle_index(self,length):
#         if length % 2 == 0:
#             return (length / 2) - 1
#         else:
#             return (length - 1) / 2
#
#     # here, keep calling helper method to get new middle index.
#     # keep running track of current middle index until loop over. then loop again and return node at that index
#     def find_middle_node(self):
#         middle_index = 0
#         length = 0
#         current = self.head
#         while current:
#             length += 1
#             middle_index = self.find_middle_index(length)
#             current = current.next
#
#         node_index = 0
#         current = self.head
#         while current.next:
#             if node_index == middle_index:
#                 return current
#             current = current.next
#             node_index += 1
#         return current
