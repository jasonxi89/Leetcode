"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    # def preorderTraversal(self, root):
    #     # write your code here
    #     result = []
    #     self.helper(root)
    #     return result
    #
    # def helper(self, root):
    #     if not root:
    #         return
    #     self.result.append(root.val)
    #     self.helper(root.left)
    #     self.helper(root.right)
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            curr_node = stack.pop()
            result.append(curr_node.val)
            #因为我们想先加左边的，所以就把右边的根先丢进去，然后再丢左边，其实一样，用deque可以选方向
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)

        return result




    # def preorderTraversal(self, root):
    #     self.results = []
    #     self.traverse(root)
    #     return self.results
    #
    # def traverse(self, root):
    #     if root is None:
    #         return
    #     self.results.append(root.val)
    #     self.traverse(root.left)
    #     self.traverse(root.right)