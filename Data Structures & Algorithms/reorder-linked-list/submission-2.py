# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
            # reverse 1 to n, 2 to n until 1 element left 
            head
            while head.next:
                reversed_list_head = self.reverse(head.next)
                head.next = reversed_list_head
                head = head.next
            return

