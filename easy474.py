"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    # node, foundA,foundB = None, False, False
    def lowestCommonAncestorII(self, root, A, B):
        if (not root) or (root == A) or ( root == B):
            return root

        root_left = self.lowestCommonAncestorII(root.left,A,B)
        root_right = self.lowestCommonAncestorII(root.right,A,B)

        if(root_left != None and root_right != None):
            return root

        if root_right != None:
            return root_right

        if root_left != None:
            return root_left

        return None

