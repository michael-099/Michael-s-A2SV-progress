# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=head
        right=head.next
        while right:
            left=left.next
            right=right.next
            if right:
               right= right.next
            else:
                break
        return left