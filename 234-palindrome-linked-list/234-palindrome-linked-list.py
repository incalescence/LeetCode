# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # copy the values into a list 
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        
        reversed_values = values[::-1]
        
        if reversed_values == values:
            return True
        else:
            return False
            
        