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

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        # 思路：从最左边开始排着找？如果找到了
    def helper(self,root,k):
        if not root:
            return
        self.helper(root.left)

