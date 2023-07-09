# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        right=head
        left=dummy
        i=0
        while right and i<n:
            right =right.next
            i=i+1
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next