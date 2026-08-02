# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head):
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse_head = self.reverse_list(slow)
        original_head = head

        while original_head and reverse_head:
            if (original_head.val != reverse_head.val):
                return False
            original_head = original_head.next
            reverse_head = reverse_head.next
        
        return True


        
        