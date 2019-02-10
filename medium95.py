"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        95. 验证二叉查找树
        中文English
        给定一个二叉树，判断它是否是合法的二叉查找树(BST)

        一棵BST定义为：

        节点的左子树中的值要严格小于该节点的值。
        节点的右子树中的值要严格大于该节点的值。
        左右子树也必须是二叉查找树。
        一个节点的树也是二叉查找树。
        样例
        一个例子：

          2
         / \
        1   4
           / \
          3   5
        上述这棵二叉树序列化为 {2,1,4,#,#,3,5}.
"""

# class Solution:
#     """
#     @param root: The root of binary tree.
#     @return: True if the binary tree is BST, or false
#     """
#     def isValidBST(self, root):
#         return self.helper(root)
#         # write your code here
#     def helper(self,root):
#         if not root:
#             return True
#         if (root.left is None and root.right is not None) or (root.right is None and root.left is not None):
#             return False
#
#         leftBst = self.helper(root.left)
#         rightBst = self.helper(root.right)
#
#         if leftBst == rightBst == True:
#             if root.left and root.right:
#                 return root.left < root.val < root.right
#
#         return False
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        if root is None:
            return True

        stack = []
        while root:
            stack.append(root)
            root = root.left

        last_node = stack[-1]
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            # the only difference compare to an inorder traversal iteration
            # this problem disallowed equal values so it's <= not <
            if stack:
                if stack[-1].val <= last_node.val:
                    return False
                last_node = stack[-1]
        return True
