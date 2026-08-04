# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        current = head
        previous = None

        while current:
            next_node = current.next

            current.next = previous
            previous = current
            current = next_node
        
        return previous

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        slow, fast = ListNode(next=head), head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first_half = head
        second_half = slow.next
        slow.next = None

        second_half = self.reverseList(second_half)

        while first_half and second_half:
            first_half_next = first_half.next
            second_half_next = second_half.next if second_half else None

            first_half.next = second_half
            if first_half_next:
                second_half.next = first_half_next
                second_half = second_half_next
                first_half = first_half_next
            else:
                first_half.next = second_half
                second_half = None

        

        

