"""
    Definition of TreeNode:
    class TreeNode:
        def __init__(self, val):
            this.val = val
            this.left, this.right = None, None
    Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

        给一棵二叉树，设计一个算法为每一层的节点建立一个链表。也就是说，如果一棵二叉树有D层，那么你需要创建D条链表。

    样例
    对于二叉树：

        1
       / \
      2   3
     /
    4
    返回3条链表：

    [
      1->null,
      2->3->null,
      4->null
    ]
"""
import collections
# class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    #思路：ROOT开始读，BFS，读完一圈以后加NULL
    # def binaryTreeToLists(self, root):
    #     # Write your code here
    #     if not root:
    #         return []
    #     queen = collections.deque[root]
    #     ret = []
    #     while not queen:
    #         level= queen[0]
    #         level_first = queen[0]
    #         for _ in range(len(queen)):
    #             curr = queen.popleft()
    #             if not curr.left:
    #                 queen.append(curr.left)
    #             if not curr.right:
    #                 queen.append(curr.right)
    #             level.next = curr
    #         ret.append(level_first)
    #     return ret
    # 需要个哨兵以及最后一个点
from collections import deque
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []

        queue = deque([root])
        result = []

        dummy = ListNode(0)  # 0->None
        lastNode = None

        while queue:
            lastNode = dummy  # initial

            for _ in range(len(queue)):
                node = queue.popleft()

                lastNode.next = ListNode(node.val)  # connect
                lastNode = lastNode.next  # move

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(dummy.next)

        return result




