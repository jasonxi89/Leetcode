"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        902. BST中第K小的元素
        中文English
        给一棵二叉搜索树，写一个 KthSmallest 函数来找到其中第 K 小的元素。

        样例
        给定 root = {1,#,2}, k = 2, 返回 2.

        挑战
        如果这棵 BST 经常会被修改(插入/删除操作)并且你需要很快速的找到第 K 小的元素呢？你会如何优化这个 KthSmallest 函数？

        注意事项
        你可以假设 k 总是有效的， 1 ≤ k ≤ 树的总节点数。
"""
import sys
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    # def kthSmallest(self, root, k):
    #     # write your code here
    #     # 思路：从最左边开始排着找？如果找到了开始计数，但是感觉并不行，我是不是需要个计数器？从左边开始rec,还是说我写个数组？
    #     #
    #     ret = self.find(root,[])
    #     return ret[k-1]
    # def find(self,root, order_set):
    #     order_set = []
    #     if not root:
    #         return order_set
    #     order_set.append(self.find(root.left, order_set))
    #     if root.left is None:
    #         order_set.append(root.val)
    #     order_set.append(self.find(root.right,order_set))
    #     return order_set

    # def kthSmallest(self, root, k):
    #     # use binary tree iterator
    #
    #     stack = []
    #     #把所有的放进stack里
    #     while root:
    #         stack.append(root)
    #         root = root.left
    #     #开始循环，循环K次
    #     for i in range(k - 1):
    #         if not stack:
    #             break
    #         #如果stack的最右边有right(也就是最后加进来的)
    #         if stack[-1].right:
    #             #那么判断下这个right,是不是还有left,有的话加进stack里
    #             node = stack[-1].right
    #             while node:
    #                 stack.append(node)
    #                 node = node.left
    #         #这个点没有没有right
    #         else:
    #             #那么从最后加的点Pop出去
    #             node = stack.pop()
    #             #如果stack不是空的，并且最后一个点的右边是Node
    #             while stack and stack[-1].right == node:
    #                 node = stack.pop()
    #
    #     return stack[-1].val
    # import sys
    def kthSmallest(self, root, k):
        self.kth = k
        self.val = sys.maxsize
        self.dfs(root)
        return self.val
    def dfs(self,root):
        if not root: return
        self.dfs(root.left)
        self.kth -= 1
        if self.kth ==0:self.val = root.val
        self.dfs(root.right)


