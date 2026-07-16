# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reversedNumbderList(self, head: Optional[ListNode]):
        if head == None:
            return []
        if head.next is None:
            return [head.val]
        return self.reversedNumbderList(head.next) + [head.val]

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = self.reversedNumbderList(head)
        if len(newList) == 0:
            return None
        head = ListNode(newList[0])
        oriHead = head
        for i in range(1, len(newList)):
            head.next = ListNode(newList[i])
            head = head.next
        return oriHead