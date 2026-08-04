# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        slowed = ListNode(next=head)

        if head is None or head.next is None:
            return None

        while fast and fast.next:
            slowed = slowed.next
            slow = slow.next
            fast = fast.next.next
        
        slowed.next = slowed.next.next

        return head
        