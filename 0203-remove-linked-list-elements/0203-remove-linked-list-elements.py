# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            if previous is None and current.val == val:
                head = current.next
            elif current.val != val:
                previous = current
            else:
                previous.next = current.next
            
            current = current.next

        return head
        