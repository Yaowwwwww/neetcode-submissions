# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        D = ListNode()
        D.next = head
        L = D
        
        R = D
        for i in range(n + 1):
            R = R.next

        while R:
            L = L.next
            R = R.next
        
        L.next = L.next.next

        return D.next
