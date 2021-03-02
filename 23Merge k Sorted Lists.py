# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        if amount==0:
            return None
        
        while interval < amount:
            for i in range(0,amount-interval,interval*2):
                lists[i] = self.mergeTwoLists(lists[i],lists[i+interval])
            interval*=2
        return lists[0] 
        
                
    def mergeTwoLists(self,l1,l2):
        head = point = ListNode(0)
        
        while l1 and l2:
            if l1.val<=l2.val:
                point.next = l1  
                l1 = l1.next
                point = point.next
            else:
                point.next = l2       
                l2= l2.next
                point = point.next
                
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
        
        
# Approach3: use heapq  time:O(Nlogk)    
#O(n) Creating a new linked list costs O(n) space.
#O(k) The code above present applies in-place method which cost
#         head = point = ListNode(0)
#         h=[]
#         for idx,l in enumerate(lists):
#             if l:
#                 h.append((l.val, idx))
#         heapq.heapify(h)
#         while h:
#             val,idx = heapq.heappop(h)
#             point.next = ListNode(val)
#             point = point.next
#             lists[idx]=lists[idx].next
#             node = lists[idx]
#             if node:
#                 heapq.heappush(h,(node.val,idx))
#         return head.next
    
    
       

        
# Appprach TW0: compare one by one        
#         head = point = ListNode(0)
#         k = len(lists)
        
#         empty = False
        
#         while not empty:
#             empty = True
#             minval = float('inf')
#             for i in range(k):
#                 if lists[i]:
#                     empty = False
#                     if lists[i].val < minval:
#                         minval,idx = lists[i].val,i
#             if not empty:
#                 head.next = lists[idx]
#                 head = head.next
#                 lists[idx] = lists[idx].next
        
#         return point.next
            
                    
        
    

    
    
    
    
#  Brute Force
#         nodes=[]
#         head = point = ListNode(0)
#         for l in lists:
#             while l:
#                 nodes.append(l.val)
#                 l=l.next
        
#         for x in sorted(nodes):
#             point.next = ListNode(x)
#             point = point.next
#         return head.next
        