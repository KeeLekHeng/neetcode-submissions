# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        prev = None
        curr = head

        #get length of linked list
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        toRemove = count - n
        count = 0

        while curr:
            if count == toRemove:
                if prev is None and curr.next is None:
                    head = None
                elif prev is None:
                    head = curr.next
                elif curr.next is None: 
                    prev.next = None
                else:
                    prev.next = curr.next
                return head
                      
            else:
                count += 1
                temp = curr.next
                prev = curr
                curr = temp



