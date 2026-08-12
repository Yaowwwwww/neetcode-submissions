# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        q = []
        
        #先都放每个list的第一个元素到q 然后维护这个长度每次分别pop加入
        for i in range(n):
            if lists[i]:
                heapq.heappush(q,(lists[i].val, i))
                lists[i] = lists[i].next#删除当前
        res = ListNode()
        cur = res
        while q:
            val, i = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i] is not None:
                heapq.heappush(q,(lists[i].val, i))
                lists[i] = lists[i].next
        return res.next


        