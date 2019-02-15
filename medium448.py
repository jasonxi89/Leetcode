"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    中序
    用successor维护前一位，左子树如果一直比p值大则一直向左找，一旦左节点值大于p则p一定在右子树上
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        stack = []
        inorder = []
        curr_node = root
        while stack or curr_node:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left

            curr_node = stack.pop()
            inorder.append(curr_node)
            curr_node = curr_node.right
        index = inorder.index(p)+1
        if index < len(inorder):
            return inorder[index]
        return None

