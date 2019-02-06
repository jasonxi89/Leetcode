"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    480. 二叉树的所有路径
    给一棵二叉树，找出从根节点到叶子节点的所有路径。

    样例
    例1：

    输入：

       1
      / \
    2   3
     \
      5

    输出：


    [
      "1->2->5",
      "1->3"
    ]
    例2：

    输入：

       1
     /
    2


    输出：

    [
      "1->2"
    ]
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)

        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)

        return paths