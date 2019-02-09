"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    94. 二叉树中的最大路径和
    中文English
    给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束（路径和为两个节点之间所在路径上的节点权值之和）

    样例
    给出一棵二叉树：

           1
          / \
         2   3
    返回 6
    """

# class Solution:
#     """
#     @param root: The root of binary tree.
#     @return: An integer
#     """
#     def maxPathSum(self, root):
#         # write your code here
#         if not root:
#             return 0
#         leftMax = self.maxPathSum(root.left)
#
#         rightMax = self.maxPathSum(root.right)
#
#         return max(leftMax,rightMax)+root.val
#     def helper(self,root):
#         #好像不太行，需要判断下？连续节点是不是比绝对值大？或者直接存着最大值跑？
#




# 由于这是一个很简单的例子，我们很容易就能找到最长路径为7-11-4-13，那么怎么用递归来找出正确的路径和呢？根据以往的经验，树的递归解法一般都是递
# 归到叶节点，然后开始边处理边回溯到根节点。那么我们就假设此时已经递归到结点7了，那么其没有左右子节点，所以如果以结点7为根结点的子树最大路径和
# 就是7。然后回溯到结点11，如果以结点11为根结点的子树，我们知道最大路径和为7+11+2=20。但是当回溯到结点4的时候，对于结点11来说，就不能同时取
# 两条路径了，只能取左路径，或者是右路径，所以当根结点是4的时候，那么结点11只能取其左子结点7，因为7大于2。所以，对于每个结点来说，我们要知道
# 经过其左子结点的path之和大还是经过右子节点的path之和大。那么我们的递归函数返回值就可以定义为以当前结点为根结点，到叶节点的最大路径之和，然后
# 全局路径最大值放在参数中，用结果res来表示。
#
# 在递归函数中，如果当前结点不存在，那么直接返回0。否则就分别对其左右子节点调用递归函数，由于路径和有可能为负数，而我们当然不希望加上负的路径
# 和，所以我们和0相比，取较大的那个，就是要么不加，加就要加正数。然后我们来更新全局最大值结果res，就是以左子结点为终点的最大path之和加上以右子
# 结点为终点的最大path之和，还要加上当前结点值，这样就组成了一个条完整的路径。而我们返回值是取left和right中的较大值加上当前结点值，因为我们
# 返回值的定义是以当前结点为终点的path之和，所以只能取left和right中较大的那个值，而不是两个都要
import sys
class Solution:

    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        #maxpath记录路上最大的值
        # maxPath = - sys.maxsize
        _ , maxPath= self.helper(root)
        return maxPath

    def helper(self,root):
        #返回值第一个值为当前值，第二个值位路径最大值
        if root is None:
            return 0, - sys.maxsize
        #left/right均为数组，0位置是当经过点的最大值，1位置是当顶点的最大值
        left = self.helper(root.left)
        right = self.helper(root.right)
        passValue = max(0, left[0]+root.val, right[0] + root.val)
        # maxPath = root.val + max(left[1]+right[1],0)
        # 最大值有可能是 过这个点，也有可能是以前的某个点
        maxPath = max (left[0]+right[0]+root.val, left[1], right[1])
        return passValue,maxPath



