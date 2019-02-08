"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        97. 二叉树的最大深度
        中文English
        给定一个二叉树，找出其最大深度。

        二叉树的深度为根节点到最远叶子节点的距离。

        样例
        样例  1:
            输入: tree = {}
            输出: 0

            样例解释:
            空树的深度是0。

        样例  2:
            输入: tree = {1,2,3,#,#,4,5}
            输出: 3

            样例解释:
            如下，深度是3
                  1
                 / \
                2  3
                  /  \
                 4   5
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
