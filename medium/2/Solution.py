# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        tmp1, tmp2 = l1, l2
        while tmp1 != None:
            num1 += str(tmp1.val)
            tmp1 = tmp1.next
        while tmp2 != None:
            num2 += str(tmp2.val)
            tmp2 = tmp2.next
        num1, num2 = num1[::-1], num2[::-1]
        
        result = int(num1 or "0") + int(num2 or "0")
        result = str(result)
        

        if len(num1) > len(num2):
            head = l1  
            current = l1
            tail = None  
            arr = list(result)
            
            while len(arr) != 0:
                if current == None:
                    new_node = ListNode(int(arr.pop()), None)
                    if tail:
                        tail.next = new_node
                    tail = new_node
                else :
                    current.val = int(arr.pop())
                    tail = current
                    current = current.next
            return head 
        else: 
            head = l2 
            current = l2
            tail = None  
            arr = list(result)
            
            while len(arr) != 0:
                if current == None:
                    new_node = ListNode(int(arr.pop()), None)
                    if tail:
                        tail.next = new_node
                    tail = new_node
                else :
                    current.val = int(arr.pop())
                    tail = current  
                    current = current.next
            return head 