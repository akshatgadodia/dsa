# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Find node before 'left'
        left_prev = dummy
        for _ in range(left - 1):
            left_prev = left_prev.next

        # Find 'right' node
        right_node = left_prev.next
        for _ in range(right - left):
            right_node = right_node.next

        # Split into three parts
        after_right = right_node.next
        right_node.next = None

        middle = left_prev.next
        left_prev.next = None

        # Reverse middle
        reversed_head = self.reverse_list(middle)

        # Connect first part to reversed middle
        left_prev.next = reversed_head

        # 'middle' is now the tail after reversal
        middle.next = after_right

        return dummy.next