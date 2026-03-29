# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_lists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 or l2:
            cur.next = l1 if l1 else l2        
        return dummy.next
    
    def divide_lists(self, lists, s=0, e=None):
        if e is None:
            e = len(lists)
        if (e-s) <= 1:
            return lists[s]
        
        mid = (s+e)//2
        l1 = self.divide_lists(lists, s, mid)
        l2 = self.divide_lists(lists, mid, e)
        return self.merge_lists(l1, l2)


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0 or lists is None:
            return None
        return self.divide_lists(lists)

        
        
            