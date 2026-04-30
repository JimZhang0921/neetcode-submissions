# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        cur = dummy

        l1_cur = list1
        l2_cur = list2

        while l1_cur and l2_cur:
            if l1_cur.val <= l2_cur.val:
                cur.next = l1_cur
                l1_cur = l1_cur.next
            else:
                cur.next = l2_cur
                l2_cur = l2_cur.next
            cur = cur.next
        if l1_cur:
            cur.next = l1_cur
        elif l2_cur:
            cur.next = l2_cur
        
        return dummy.next






