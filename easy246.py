"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        # write your code here
        results = []
        if root is None:
            return results
        left = self.binaryTreePathSum2(root.left, target)
        right = self.binaryTreePathSum2(root.right, target)
        middle = self.fromRootToAny(root, target)
        return left + right + middle

    def fromRootToAny(self, root, target):
        results = []
        path = []
        self.dfsHelper(root, target, results, path)
        return results

    def dfsHelper(self, root, target, results, path):
        if root is None:
            return
        path.append(root.val)
        if root.val == target:
            results.append(path[:])
        self.dfsHelper(root.left, target - root.val, results, path)
        self.dfsHelper(root.right, target - root.val, results, path)
        path.pop()