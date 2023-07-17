class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
        
        new_tail_pos = length - k
        new_tail = head
        for i in range(1, new_tail_pos):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        last_node.next = head
        
        return new_head