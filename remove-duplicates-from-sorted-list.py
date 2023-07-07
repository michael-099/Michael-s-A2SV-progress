# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        prev=None
        while temp:
            if temp.val not in arr:
                arr.append(temp.val)
                print(arr)
                prev=temp
            elif temp.val in arr:
                prev.next=temp.next
            temp=temp.next
        return head