# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        else: 
            prev = None
            curr = head
            nex = curr.next
            while curr :
                curr.next = prev
                prev = curr
                curr = nex
                if nex: 
                    nex = nex.next
        return prev
            
        