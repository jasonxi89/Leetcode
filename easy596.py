"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    596. 最小子树
    给一棵二叉树, 找到和为最小的子树, 返回其根节点。

    样例
    例1:

    输入:
         1
       /   \
     -5     2
     / \   /  \
    0   2 -4  -5

    输出:1
    例2:

    输入:
       1
    输出:1
    注意事项
    LintCode会打印根节点为你返回节点的子树。保证只有一棵和最小的子树并且给出的二叉树不是一棵空树。
"""
import sys

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        # 需要记录3个值，最小值，顶点，以及和
        minimum, subtree, sum = self.helper(root)
        return subtree

    def helper(self,root):
        if root is None:
            return sys.maxsize,None,0
        left_minimum,left_subtree,left_sum = self.helper(root.left)
        right_minimum,right_subtree,right_sum = self.helper(root.right)

        curr_sum = left_sum + right_sum + root.val

        if left_minimum == min(left_minimum,right_minimum,curr_sum):
            return left_minimum,left_subtree, curr_sum
        if right_minimum == min(left_minimum,right_minimum,curr_sum):
            return right_minimum,right_subtree,curr_sum

        return curr_sum,root,curr_sum