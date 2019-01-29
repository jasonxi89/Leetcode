"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false

    102. 带环链表
    给定一个链表，判断它是否有环。

    样例
    给出 -21->10->4->5, tail connects to node index 1，返回 true

    挑战
    不要使用额外的空间
    #一个一倍速前进，一个2倍速前进，如果有环早晚相遇
    """
    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        p1 = head
        p2 = head
        while True:
            if p1.next is not None:
                p1=p1.next.next
                p2=p2.next
                if p1 is None or p2 is None:
                    return False
                elif p1 == p2:
                    return True
            else:
                return False
        return False
