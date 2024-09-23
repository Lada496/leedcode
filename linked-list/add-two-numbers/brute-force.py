# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2, carry = l1, l2, 0
        answer = dummy = ListNode()
        while cur1 and cur2:
            val = cur1.val + cur2.val + carry
            if val >=10:
                carry = 1
                val = val - 10
            else:
                carry = 0
            dummy.next = ListNode(val)
            dummy = dummy.next
            cur1 = cur1.next
            cur2 = cur2.next

        rest = cur1 or cur2
        if rest:
            while rest:
                val = rest.val + carry
                if val >=10:
                    carry = 1
                    val = val - 10
                else:
                    carry = 0
                dummy.next = ListNode(val)
                dummy = dummy.next
                rest = rest.next

        if carry:
            dummy.next = ListNode(carry)
        return answer.next
