# https://leetcode.com/problems/binary-tree-paths/description/
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
        return []

    if root.left is None and root.right is None:
        return [str(root.val)]

    path = binaryTreePaths(root.left) + binaryTreePaths(root.right)
    return [str(root.val) + "->"  + i for i in path]
