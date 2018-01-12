# https://leetcode.com/problems/path-sum-ii/description/
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    if not root:
        return []
    else:
        if root.left is None and root.right is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        else:
            total_arr = pathSum(root.left, sum - root.val) + pathSum(root.right, sum - root.val)
            return [[root.val] + i for i in total_arr]
