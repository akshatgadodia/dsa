# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        result = head

        to_carry = 0
        while True:
            if not l1 and not l2:
                break
            
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            current_sum = l1_val + l2_val + to_carry
            to_carry = current_sum // 10
            current_sum = current_sum % 10

            next_node = ListNode()
            next_node.val = current_sum
            head.next = next_node
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if to_carry:
            next_node = ListNode()
            next_node.val = to_carry
            head.next = next_node
            head = head.next

        return result.next
        