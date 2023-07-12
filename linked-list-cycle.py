# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None :return False
        if(head.next==None ):
            return False
        left=head
        right=head.next
        temp=head
        while(right.next):
            left=left.next
            if right.next.next:
                right=right.next.next
            elif right.next:right=right.next
            if(left==right):
                print(left)
                print(right)
                return True
        return False