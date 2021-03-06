# https://leetcode.com/problems/path-sum/description/
#
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def hasPathSum(root, sum, current_sum = 0):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    else:
        current_sum += root.val
        if root.left is None and root.right is None:
            return current_sum == sum
        else:
            return hasPathSum(root.left, sum, current_sum) or hasPathSum(root.right, sum, current_sum)
