# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merg=ListNode()
        head=merg
        while list1!=None and list2!=None:
            if(list1.val<=list2.val):
                merg.next=list1
                list1=list1.next
            else:
                merg.next=list2
                list2= list2.next
            merg=merg.next
        if list1!=None:
            merg.next=list1
        if list2!=None:
            merg.next=list2
        return head.next