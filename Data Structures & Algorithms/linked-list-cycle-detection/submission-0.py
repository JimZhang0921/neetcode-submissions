# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f_ptr = head
        s_ptr = head
        while f_ptr and f_ptr.next:
            f_ptr = f_ptr.next.next
            s_ptr = s_ptr.next
            if f_ptr == s_ptr:
                return True
        return False