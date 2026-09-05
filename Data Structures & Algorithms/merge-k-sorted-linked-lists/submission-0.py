# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for i in range(len(lists)):
            currList = lists[i]
            if currList:
                heapq.heappush(heap,(currList.val, i, currList))  
        dum = ListNode()
        cur = dum
        while heap:
            val, idx, node = heapq.heappop(heap)
            nxtnode= node.next
            if nxtnode:
                heapq.heappush(heap,(nxtnode.val, idx, nxtnode))
            cur.next = node
            cur = cur.next   

            

        return dum.next     