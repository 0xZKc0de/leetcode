# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None:
            return head
        arr = []
        tmp, current = head, head
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next
        
        while k != 0:
            arr.insert(0, arr[-1])
            del arr[-1]
            k -=1
        i = 0
        while current:
            current.val = arr[i]
            current = current.next
            i +=1

        return head
        

# This solution is with complexity O(N + N*K), so it is did not pass all the tests.