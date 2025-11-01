# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_nums = set(nums)
        linkedlist = ListNode(0)
        linkedlist.next = head

        prev, tmp = linkedlist, head
        while tmp:
            if tmp.val in set_nums:
                prev.next = tmp.next
            else:
                prev = tmp
            tmp = tmp.next
        return linkedlist.next
            
