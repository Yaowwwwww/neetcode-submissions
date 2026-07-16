# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        seen.add(head.val)
        while head.next != None:
            if head.next.val in seen:
                return True
            seen.add(head.next.val)
            head = head.next
        return False
        