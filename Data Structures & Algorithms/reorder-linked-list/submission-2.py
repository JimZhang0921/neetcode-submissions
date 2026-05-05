# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prew = None
        cur = slow.next
        slow.next = None

        while cur:
            nxt = cur.next
            cur.next = prew
            prew = cur
            cur = nxt
        
        l1 = head
        l2 = prew

        while l2:
            n1 = l1.next
            n2 = l2.next

            l1.next = l2
            l2.next = n1

            l1 = n1
            l2 = n2
        
            


