# 147

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [4,2,1,3]
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        cur = head #4 # 2
        while cur:
            prev = answer # 0 # 0 -> 4
            # where to insert cur 
            while prev.next and prev.next.val <= cur.val:
                prev = prev.next
            
            # cache next
            next = cur.next #2 -> 1 -> 3 #1 -> 3

            ## insert cur to the new list
            cur.next = prev.next # 4 -> None # 2 -> 4
            prev.next = cur # 0 -> 4 # 0 -> 2 -> 4

            # move on to the next
            cur = next # 2 -> 1 -> 3
        
        return answer.next