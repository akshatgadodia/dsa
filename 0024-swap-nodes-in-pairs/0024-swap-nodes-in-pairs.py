# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printList(self, head):
        if not head:
            return
        
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        
        print("")

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        current = dummy
        while current and current.next:
            first_element = current.next
            second_element = current.next.next

            current.next = second_element if second_element else first_element
            first_element.next = second_element.next if second_element else None
            if second_element:
                second_element.next = first_element
            current = first_element

        return dummy.next