# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        arr, tmp, current = [], head, head
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next
        
        while current:
            current.val = arr.pop()
            current = current.next
        return head
    

# for reverse a linkedlist