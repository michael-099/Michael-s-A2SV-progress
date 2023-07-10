# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if head==None:
          return None
        dummy=ListNode(-101,head)
        left=dummy
        right=head
        while right:
            if right.next and right.val==right.next.val:
              while right.next and right.val==right.next.val:
                right=right.next
              left.next=right.next
            else:
                 left=left.next
            right=right.next
                
        return dummy.next