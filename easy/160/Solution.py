# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA == None or headB == None:
            return None
        linked_set = set()
        while headB:
            linked_set.add(id(headB))
            headB = headB.next
        while headA:
            if id(headA) in linked_set:
                return headA
            headA = headA.next

        return None