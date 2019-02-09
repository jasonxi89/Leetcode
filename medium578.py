"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
        578. 最近公共祖先 III
        中文English
        给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。

        两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），离这两个节点最近的公共的节点。

        返回 null 如果两个节点在这棵树上不存在最近公共祖先的话。

        样例
        给出下面这棵树：

          4
         / \
        3   7
           / \
          5   6
        LCA(3, 5) = 4
        LCA(5, 6) = 7
        LCA(6, 7) = 7
        LCA(5, 8) = null

        注意事项
        这两个节点未必都在这棵树上出现。
        """


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
