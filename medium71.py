"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


    71. 二叉树的锯齿形层次遍历
    给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行）

    样例
    给出一棵二叉树 {3,9,20,#,#,15,7},

        3
       / \
      9  20
        /  \
       15   7
    返回其锯齿形的层次遍历为：

    [
      [3],
      [20,9],
      [15,7]
    ]
"""

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def zigzagLevelOrder(self, root):
        self.results = []
        self.preorder(root, 0, self.results)
        return self.results

