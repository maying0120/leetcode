#https://blog.csdn.net/To_be_to_thought/article/details/83958314 
#Floyd cycle detection 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        if not head or not head.next:
            return None
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break
        
        if fast==slow:
            while fast!=head:
                fast = fast.next
                head = head.next
            return head
        #else: