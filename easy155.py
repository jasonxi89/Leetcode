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
    @param root: The root of binary tree
    @return: An integer
    """
    # DFS
    # def minDepth(self, root):
    #     # write your code here
    #     return self.find(root)
    #
    # def find(self, node):
    #     if node is None:
    #         return 0
    #     left, right = 0, 0
    #     if node.left != None:
    #         left = self.find(node.left)
    #     else:
    #         return self.find(node.right) + 1
    #
    #     if node.right != None:
    #         right = self.find(node.right)
    #     else:
    #         return left + 1
    #
    #     return min(left,right) + 1
    #
    #
    #
    #
    # BFS
    # def minDepth(self, root):
    #     # null case
    #     if not root:
    #         return 0
    # 
    #     # create queue to store nodes in current level
    #     queue = deque([root])
    #     depth = 0
    #
    #     # BFS
    #     while queue:
    #         depth += 1
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #
    #             # if node is leaf node
    #             if not node.left and not node.right:
    #                 return depth
    #
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)



