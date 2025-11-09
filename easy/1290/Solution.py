# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        arr.reverse()

        for i in range(0, len(arr)):
            result += arr[i] * pow(2, i)
        return result
    
