# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
     if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))
