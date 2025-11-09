# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        arr = []
        tmp = head
        while tmp:
            arr.append(id(tmp))
            tmp = tmp.next
            middle = arr[int(len(arr)/2)]
        while id(head) != middle:
            head = head.next
        return head