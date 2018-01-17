# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


def minDepth(root, current_level = 0):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return current_level

    current_level += 1
    if root.left is None and root.right is None:
        return current_level
    if root.left is not None and root.right is not None:
        return min([minDepth(root.left, current_level), minDepth(root.right, current_level)])
    elif root.left is not None and root.right is None:
        return min([minDepth(root.left, current_level)])
    elif root.right is not None and root.left is None:
        return min([minDepth(root.right, current_level)])
