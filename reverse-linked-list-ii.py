# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=ListNode()
        r=ListNode()
        headl=l
        headr=r
        temp=head
        i=1
        while temp and i<left:
            l.next=temp
            l=l.next
            temp=temp.next
            i=i+1
        # l.next=None
        #return headl.next
        while temp and i<=right:
            r.next=temp
            r=r.next
            temp=temp.next
            i=i+1
        r.next=None
        # return headr.next
        cur=headr.next
        # print(cur)
        prev=None
        while cur:
            next_n=cur.next #2 3
            cur.next=prev#None
            prev=cur
            cur=next_n#1 2
        l.next=prev
        h=headl
        if temp:
            while headl.next:
                # print(headl.val)
                headl=headl.next
                # print(headl)
            
            headl.next=temp
        return h.next