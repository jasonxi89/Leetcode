"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    # def findSubtree2(self, root):
    #     self.max = sys.maxsize
    #     # write your code here
    # #返回值记录SUM和数量
    # def helper(self,root):
    #     if not root:
    #         return 0,0
    #     stack = []
    #     stack.append(root)
    #     while root.left:
    #         stack.append(root.left)
    #         root = root.left
    #     while stack:
    # average, node = 0, None
    #     #
    #     # def findSubtree2(self, root):
    #     #     # Write your code here
    #     #     self.helper(root)
    #     #     return self.node
    #     #
    #     # def helper(self, root):
    #     #     if root is None:
    #     #         return 0, 0
    #     #
    #     #     left_sum, left_size = self.helper(root.left)
    #     #     right_sum, right_size = self.helper(root.right)
    #     #
    #     #     sum, size = left_sum + right_sum + root.val, \
    #     #                 left_size + right_size + 1
    #     #
    #     #     if self.node is None or sum * 1.0 / size > self.average:
    #     #         self.node = root
    #     #         self.average = sum * 1.0 / size
    #     #
    #     #     return sum, size
    def findSubtree2(self, root):
        self.average = 0
        self.node = None
        self.helper(root)
        return self.node
    def helper(self,root):
        if not root:
            return 0,0

        left_sum,left_size = self.helper(root.left)
        right_sum,right_size  = self.helper(root.right)

        sum, size = left_sum + right_sum + root.val, \
                    left_size + right_size + 1

        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size

        return sum,size

