# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = l1

        while l1 and l2:
            res = l1.val + l2.val + carry
            if res >= 10:
                l1.val = res % 10
                carry = 1
            else:
                carry = 0
                l1.val = res
            
            if l1.next is None and l2.next is None and carry == 0:
                break

            if l1.next: 
                l1 = l1.next
            else:
                l1.next = ListNode()
                l1 = l1.next

            if l2.next:
                l2 = l2.next
            else:
                l2.next = ListNode()
                l2 = l2.next
        
        return head
