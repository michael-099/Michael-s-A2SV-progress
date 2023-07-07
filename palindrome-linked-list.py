# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        b=a[::-1]
        if a==b:
            return True 
        else:return False