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
    @return: The node where the cycle begins. if there is no cycle, return null
    103. 带环链表 II
    给定一个链表，如果链表中存在环，则返回到链表中环的起始节点，如果没有环，返回null。

    样例
    给出-21->10->4->5，返回10
    解释：
    最后一个节点5指向下标为1的节点，也就是10，所以环的入口为10

    挑战
    不使用额外的空间

    难的是方法，判断是否有环用个2倍速就行。如果要找到入口，就需要把头再给一次慢速的，这样的话就能找到入口，我也不知道为啥
    """
    def detectCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None