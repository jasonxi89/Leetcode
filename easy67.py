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
    @return: Inorder in ArrayList which contains node values.
    """
    # def inorderTraversal(self, root):
    #     # write your code here
    #     if root is not None:
    #         return None
    #     #中序遍历，先左再中最后右
    #     # stack  = [root]
    #     # result = []
    #     # while root.left:
    #     #     stack.append(root.left)
    #     #     root = root.left
    #     # #stack里都是最左边
    #     # while stack:
    #     #     curr_node = stack.pop()
    #     #     result.append(curr_node)
    #     #     while curr_node.right:
    #     #         #如果右边的树不是空的,把右边的树的值拿过来
    #     #         temp = curr_node.right
    #     #         while temp.left:
    #     #             stack.append(temp.left)
    #     #             temp = temp.left
    #     #         stack.append(curr_node)
    #     stack = [root]
    #     curr = root
    #     res = []
    #     while stack and curr is not None:
    #         while curr is not None:
    #             stack.append(curr)
    #             curr = curr.left
    #         if stack:
    #             curr = stack.pop()
    #             res.append(curr)
    #             curr = curr.right
    #
    #     return res
    # 想法是一样的，不过这么写更简略？
    # def inorderTraversal(self, root):
    #     if root is None:
    #         return []
    #
    #     # 创建一个 dummy node，右指针指向 root
    #     # 并放到 stack 里，此时 stack 的栈顶 dummy
    #     # 是 iterator 的当前位置
    #     dummy = TreeNode(0)
    #     dummy.right = root
    #     stack = [dummy]
    #
    #     inorder = []
    #     # 每次将 iterator 挪到下一个点
    #     # 也就是调整 stack 使得栈顶到下一个点
    #     while stack:
    #         node = stack.pop()
    #         if node.right:
    #             node = node.right
    #             while node:
    #                 stack.append(node)
    #                 node = node.left
    #         if stack:
    #             inorder.append(stack[-1].val)
    #
    #     return inorder
    # 需要的改动仅仅调换一下节点访问的次序，先序是先访问，再入栈；
    # 而中序则是先入栈，弹栈后再访问，再考虑右边
    def inorderTraversal(self, root):
        if root == None:
            return []

        stack = []
        output = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            output.append(node.val)

            node = node.right
        return output






