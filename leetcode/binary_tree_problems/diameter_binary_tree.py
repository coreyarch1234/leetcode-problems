# 
#
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.answer = 0

    def max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

    def getBinaryDiameter(self, root):
        if not root:
            return 0
        left_count = self.max_depth(root.left)
        right_count = self.max_depth(root.right)
        self.answer = max(self.answer, left_count + right_count)
        if left_count > right_count:
            return self.getBinaryDiameter(root.left)
        else:
            return self.getBinaryDiameter(root.right)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.getBinaryDiameter(root)
        return self.answer



# or

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution(object):
#     def max_depth(self, root):
#         if not root:
#             return 0
#         return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
#
#     def get_max_diameter(self, root):
#         if not root:
#             return 0
#         left_path_count = self.max_depth(root.left)
#         right_path_count = self.max_depth(root.right)
#         return left_path_count + right_path_count
#
#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root:
#             root_count = self.get_max_diameter(root)
#             left_count = self.get_max_diameter(root.left)
#             right_count = self.get_max_diameter(root.right)
#             if root_count > left_count and root_count > right_count:
#                 return root_count
#             if left_count > right_count:
#                 return self.diameterOfBinaryTree(root.left)
#             else:
#                 return self.diameterOfBinaryTree(root.right)
#         else:
#             return 0
