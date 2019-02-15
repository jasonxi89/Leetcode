class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    left mid right
    """
    # def inorderPredecessor(self, root, p):
    #     # write your code here
    #     if not root or not p:
    #         return None
    #     stack = [root]
    #     inorder = []
    #     while stack :
    #         curr_node = stack.pop()
    #         while curr_node:
    #             stack.append(curr_node)
    #             curr_node = curr_node.left
    #
    #         curr_node = stack.pop()
    #         #把最后一个节点拿出来
    #         if curr_node == p:
    #             if not inorder:
    #                 return None
    #             return inorder[-1]
    #         inorder.append(curr_node)
    #         if curr_node.right:
    #             stack.append(curr_node.right)
    #
    #     return None
    # 写错了，循环的时候默认是最左边的点，左中右，但是顶点进来并不行，左右最好是root.left = root?
    def inorderPredecessor(self, root, p):
        if not root or not p:
            return None
        stack = []
        result = []
        curr_node = root
        while stack or curr_node:
            #当前节点，如果有左节点，就丢stack里,不能判断curr_node.left,容易右边进来炸
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left

            #拿出stack最右边的点
            curr_node = stack.pop()
            #如果最右边的点是要找的，那么返回result里的最后一点
            if curr_node == p:
                if not result:
                    return None
                return result[-1]
            #如果不是，那么把这个点丢进顺序里,并且看看他右边的点
            result.append(curr_node)
            curr_node = curr_node.right


        return None