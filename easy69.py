"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    69. 二叉树的层次遍历
    给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）

    样例
    给一棵二叉树 {3,9,20,#,#,15,7} ：

      3
     / \
    9  20
      /  \
     15   7
    返回他的分层遍历结果：

    [
      [3],
      [9,20],
      [15,7]
    ]
    挑战
    挑战1：只使用一个队列去实现它

    挑战2：用BFS算法来做
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result