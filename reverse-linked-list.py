# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous=None
        current=head
        # print(current.val)
        while  current!= None:
            Next=current.next
            current.next=previous
            previous=current 
            current=Next
            # Next=current.next
        return previous