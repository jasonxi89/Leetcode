"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
        578. 最近公共祖先 III
        中文English
        给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。

        两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），离这两个节点最近的公共的节点。

        返回 null 如果两个节点在这棵树上不存在最近公共祖先的话。

        样例
        给出下面这棵树：

          4
         / \
        3   7
           / \
          5   6
        LCA(3, 5) = 4
        LCA(5, 6) = 7
        LCA(6, 7) = 7
        LCA(5, 8) = null

        注意事项
        这两个节点未必都在这棵树上出现。
        """


# class Solution:
#     """
#     @param: root: The root of the binary tree.
#     @param: A: A TreeNode
#     @param: B: A TreeNode
#     @return: Return the LCA of the two nodes.
#     """
#     def lowestCommonAncestor3(self, root, A, B):
#         # write your code here
#         if not root:
#             return None
#         self.foundA=False
#         self.foundB=False
#         self.res = None
#         self.helper(root,A,B)
#         return self.res

#     def helper(self, root,A,B):


#         # if root.left is not None:
#         #     self.helper(root.left, A, B)
#         # if root.right is not None:
#         #     self.helper(root.right,A,B)


#         # if root == A:
#         #     self.foundA = True
#         # if root == B:
#         #     self.foundB = True
#         # #如果都发现了，且res没有被赋值过，则返回root的值
#         # if self.foundA == True and self.foundB == True and self.res==None and root!=A and root !=B:
#         #     self.res = root
#         #问题出在怎么判断这个A=2和B=1的关系，如果{2,1,3}，{2,1}怎么判断这个ROOT如果是A或者是B，然后下面已经有过了
#         #先判断ROOT是不是点之一？然后遍历？

#         if root.left is not None:
#             self.helper(root.left, A, B)
#         if root.right is not None:
#             self.helper(root.right,A, B)


#         if root == A:
#             self.foundA = True
#         if root == B:
#             self.foundB = True
#         if (root == A and self.foundB == True) or (root == B and self.foundA == True) or( root==A and root ==B ):
#             self.res = root
#         if self.foundA == True and self.foundB == True and self.res==None and root !=A and root !=B:
#             self.res = root
#         #如果都发现了，且res没有被赋值过，则返回root的值
#         #如果先判断怎么样？会遇到的情况大概就是3种：1.啥都没有2.下面有一个，自己是另一个3.不在下面但是也是一个，抄个答案
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # null case
        if not root or not A or not B:
            return None

        # parameter indicates if A/B is in tree
        self.foundA = False
        self.foundB = False

        # find LCA
        lca = self.findLCA(root, A, B)

        # check if A and B in tree
        if self.foundA and self.foundB:
            return lca
        return None

    # helper function to find LCA, return None/A/B
    def findLCA(self, node, A, B):
        # null case
        if not node:
            return None

        # get left/right subtree's LCA
        left_lca = self.findLCA(node.left, A, B)
        right_lca = self.findLCA(node.right, A, B)

        # if node is A/B, found A/B
        if node is A:
            self.foundA = True
        if node is B:
            self.foundB = True

        # check if node is A or B or left/right LCA is not None
        if node in (A, B) or (left_lca and right_lca):
            return node
        return left_lca or right_lca or None






