# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head

        current = ListNode()
        current.next = head

        while current:
            if current.next and current.next.val >= x:
                break
            current = current.next

        if current is None:
            return head

        start = current
        current = current.next

        result = ListNode()
        result.next = head
        if head.val >= x :
            result = start
        
        while current and current.next:
            if current.next.val < x:
                element = current.next
                current.next = current.next.next

                element.next = start.next
                start.next = element
                start = start.next
            else:
                current = current.next
        
            print("current", current, "start", start)


        return result.next