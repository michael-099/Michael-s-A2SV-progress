# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        even=ListNode()
        odd=ListNode()
        even_head=even
        odd_head=odd
        i=0
        while temp:
            if(i % 2!=0):
                odd.next=temp
                o=odd
                odd=odd.next
            else:
                even.next=temp
                even=even.next
            i=i+1
            temp=temp.next
            odd.next=None
            even.next=odd_head.next
        return even_head.next