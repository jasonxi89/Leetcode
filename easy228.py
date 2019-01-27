"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    228. 链表的中点
    找链表的中点。

    样例
    样例 1:

    输入:  1->2->3
    输出: 2
    样例解释: 返回中间节点的值
    样例 2:

    输入:  1->2
    输出: 1
    样例解释: 如果长度是偶数，则返回中间偏左的节点的值。
    挑战
    如果链表是一个数据流，你可以不重新遍历链表的情况下得到中点么？

    ##2个指针，一个快一个慢
    """
    def middleNode(self, head):
        # write your code here
        if not head:
            return None
        spointer, fpointer = head, head
        while fpointer.next != None:
            fpointer = fpointer.next
            if fpointer.next != None:
                fpointer = fpointer.next
            else:
                return spointer
            spointer = spointer.next

        return spointer