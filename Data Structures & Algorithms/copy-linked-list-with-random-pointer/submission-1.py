"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step1: insert copied nodes
        cur = head

        while cur:
            new_node = Node(cur.val)

            new_node.next = cur.next
            cur.next = new_node

            cur = new_node.next

        # Step2: connect random
        cur = head

        while cur:
            if cur.random:
                cur.next.random = cur.random.next

            cur = cur.next.next

        # Step3: split lists
        old = head
        new = head.next

        new_head = head.next

        while old:
            old.next = old.next.next

            if new.next:
                new.next = new.next.next

            old = old.next
            new = new.next

        return new_head
        

        