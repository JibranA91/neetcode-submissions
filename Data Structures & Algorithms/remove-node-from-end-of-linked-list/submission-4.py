# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        q = dummy = ListNode(next=head)
        p = head
        for i in range(n):
            p = p.next
        
        while p:
            p = p.next
            q = q.next
        
        q.next = q.next.next
        return dummy.next




    #            R
    # [1,2,3,4,5,6,7,8,9]
    #  q     p
    #            q     p
