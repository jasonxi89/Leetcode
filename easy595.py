"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# class Solution:
#     """
#     @param root: the root of binary tree
#     @return: the length of the longest consecutive sequence path
#     """
#     def longestConsecutive(self, root):
#         # write your code here
#         return self.helper(root,None,0)
#
#     def helper(self,root,parent,clen):
#         if not root:
#             return clen
#         if parent is not None and parent.val + 1 == root.val:
#             clen +=1
#         else:
#             clen = 1
#         return max(len,self.helper(root.left,root,clen),self.helper(root.right,root,clen))
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        return self.helper(root, None, 0)

    def helper(self, root, parent, len):
        if root is None:
            return len

        if parent != None and root.val == parent.val + 1:
            len += 1
        else:
            len = 1
        return max(len, max(self.helper(root.left, root, len), \
                            self.helper(root.right, root, len)))