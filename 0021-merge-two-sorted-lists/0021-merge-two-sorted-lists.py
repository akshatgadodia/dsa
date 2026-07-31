# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1        # attach list1's node
                list1 = list1.next       # advance list1
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next             # advance tail to the node just attached
        # one list is now empty; attach whatever remains of the other
        tail.next = list1 if list1 else list2
        return dummy.next