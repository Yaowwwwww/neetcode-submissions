# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy =  ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev

            #迭代找到kth以及groupNext以便于翻转group
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            #遍历完成， 默认足够k个→设置groupnext
            groupNext = kth.next

            groupStart = groupPrev.next
            #开始翻转
            prev = groupNext
            curr = groupPrev.next
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            groupPrev.next = kth
            groupPrev = groupStart

