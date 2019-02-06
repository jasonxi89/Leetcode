"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        描述
        给一棵非空二叉搜索树以及一个target值，找到在BST中最接近给定值的节点值

        给出的目标值为浮点数
        我们可以保证只有唯一一个最接近给定值的节点
        您在真实的面试中是否遇到过这个题？
        样例
        样例1

        输入: root = {5,4,9,2,#,8,10} and target = 6.124780
        输出: 5
        样例2

        输入: root = {3,2,4,1} and target = 4.142857
        输出: 4
"""
import sys
import math

class Solution:

    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    #递归写贼傻逼
    """

    def closestValue(self, root, target):
        #return的是值
        #找到出在哪个位置
        if root is None:
            return None

    #取最小边界值
    def get_lower_bound(self, root, target):
        if root is None:
            return None
        #如果目标值小于当前的节点值
        if target < root.val:
            # 那最小值一定在左边
            return self.get_low_bound(root,target)
        #如果目标值大于当前的节点值，那最小值一定在右边
        lower = self.get_lower_bound(root.right, target)
        return root if lower is None else lower

    def get_upper_bound(self, root, target):
        # get the smallest node that >= target
        if root is None:
            return None

        if target >= root.val:
            return self.get_upper_bound(root.right, target)

        upper = self.get_upper_bound(root.left, target)
        return root if upper is None else upper





    # def closestValue(self, root, target):
    #     # 不停的比较自己的
    #     # write your code here
    #     def get_lower_bound(self, root, target):
    #         # get the largest node that < target
    #         if root is None:
    #             return None
    #
    #         if target < root.val:
    #             return self.get_lower_bound(root.left, target)
    #
    #         lower = self.get_lower_bound(root.right, target)
    #         return root if lower is None else lower
    #
    #     def get_upper_bound(self, root, target):
    #         # get the smallest node that >= target
    #         if root is None:
    #             return None
    #
    #         if target >= root.val:
    #             return self.get_upper_bound(root.right, target)
    #
    #         upper = self.get_upper_bound(root.left, target)
    #         return root if upper is None else upper
    #
    #
    #     if root is None:
    #         return None
    #     lower = get_lower_bound(root, target)
    #     upper = get_upper_bound(root, target)
    #     if lower is None:
    #         return upper.val
    #     if upper is None:
    #         return lower.val
    #
    #     if target - lower.val < upper.val - target:
    #         return lower.val
    #     return upper.val


