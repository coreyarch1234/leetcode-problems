# https://leetcode.com/problems/sum-of-left-leaves/description/
#
#
# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


def sumOfLeftLeaves(root, left_sum = 0):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    if root.left:
        if not root.left.left and not root.left.right:
            left_sum = root.left.val
            return left_sum + sumOfLeftLeaves(root.right)
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
    if root.right:
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)

    if not root.left and not root.right:
        return 0
