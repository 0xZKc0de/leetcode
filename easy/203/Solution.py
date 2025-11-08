# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dommy_linkedlist = ListNode(0, head)
        previous = dommy_linkedlist
        while previous.next:
            if previous.next.val != val:
                previous = previous.next
            else:
                previous.next = previous.next.next
        
        return dommy_linkedlist.next