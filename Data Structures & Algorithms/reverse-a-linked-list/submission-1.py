# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = reverse
            reverse = cur
            cur = next_node
        return reverse


