# ref: https://leetcode.com/problems/add-two-numbers/editorial/comments/237685
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2, sum = l1, l2, 0
        answer = dummy = ListNode()
        while cur1 or cur2:
            if cur1:
                sum = sum + cur1.val
                cur1 = cur1.next
            if cur2:
                sum = sum + cur2.val
                cur2 = cur2.next
            dummy.next = ListNode(sum % 10)
            dummy = dummy.next
            
            sum = 1 if sum >= 10 else 0
        if sum:
            dummy.next = ListNode(sum)
        return answer.next
