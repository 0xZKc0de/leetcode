# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        i, j = 0, len(lst) - 1
        while i <= j:
            if lst[i] != lst[j]:
                return False
            i +=1
            j -=1
        return True

