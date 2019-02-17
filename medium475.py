"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # write your code here
        if not root:
            return 0
        return max(self.maxPathSum2(root.left),self.maxPathSum2(root.right),0)+root.val