# https://leetcode.com/problems/symmetric-tree/description/
#
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Time Spent: could not solve


def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    node_q = []
    node_q.append(root)
    node_q.append(root)
    while len(node_q) != 0:
        t1 = node_q.pop()
        t2 = node_q.pop()
        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        node_q.append(t1.left)
        node_q.append(t2.right)
        node_q.append(t1.right)
        node_q.append(t2.left)
    return True
