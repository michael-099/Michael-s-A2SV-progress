# Definition for singly-linked list.
# class ListNode:
#     def init(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast =head 
        flag=False
        while fast and  fast.next:
              slow=slow.next
              fast=fast.next.next
              if fast==slow:
                  flag=True
                  break

        while head!=slow and flag==True:
                head=head.next
                slow=slow.next 
        if flag==False:return None  
        return slow