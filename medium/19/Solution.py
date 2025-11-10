# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        if not head:
            return None
        while tmp:
            length +=1
            tmp = tmp.next

        if length == 1:
            return 
        if length == n:
            head = head.next
        current = head
        while current:
            if length - 1 == n:
                print(current.val)
                current.next = current.next.next
                length -=1
            else:
                current = current.next
                length -=1
        return head
