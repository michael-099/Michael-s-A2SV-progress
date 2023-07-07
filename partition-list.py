# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node=head
        max_node=ListNode()
        max_head=max_node
        min_node=ListNode()
        min_head=min_node
        print(x)
        while node:
            if node.val>=x:
                print(f'if{node.val}')
                max_node.next=node
                max_node=max_node.next
            elif node.val<x :
                print(f'else{node.val}')
                min_node.next=node
                min_node=min_node.next
            node=node.next
        max_node.next=None
        min_node.next=max_head.next
        return min_head.next