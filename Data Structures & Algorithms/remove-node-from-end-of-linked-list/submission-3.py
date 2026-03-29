# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dum_head = ListNode(next=head)

        l_len = 0
        cur = head
        while cur:
            l_len += 1
            cur = cur.next
        
        if l_len <= 1:
            return None

        cur = dum_head
        for i in range(l_len-n):
            cur = cur.next
        
        cur.next = cur.next.next

        return dum_head.next
