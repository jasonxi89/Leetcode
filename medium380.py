"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    380. 两个链表的交叉
    请写一个程序，找到两个单链表最开始的交叉节点。

    样例
    下列两个链表：

    A:          a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗
    B:     b1 → b2 → b3
    在节点 c1 开始交叉。

    挑战
    需满足 O(n) 时间复杂度，且仅用 O(1) 内存。

    注意事项
    如果两个链表没有交叉，返回null。
    在返回结果后，两个链表仍须保持原有的结构。
    可假定整个链表结构中没有循环。
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA:
            return None
        if not headB:
            return None
        dict ={}
        while headA != None:
            dict[headA] = 1
            headA = headA.next
        while headB != None:
            if dict.get(headB) != None:
                return headB
            else:
                headB = headB.next
        return None