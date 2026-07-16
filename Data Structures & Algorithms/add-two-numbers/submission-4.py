# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getReverse(L):
            R = [str(L.val)]
            while L.next:
                L = L.next
                R = [str(L.val)] + R
            return R
         
        def breakDown(I):
            L = [int(x) for x in str(I)][::-1]
            print(L)
            R = ListNode()
            dummy = R
            for i, x in enumerate(L):
                R.val = x
                if i == len(L) - 1:
                    break
                R.next = ListNode()
                R = R.next
            return dummy

        a = int("".join(getReverse(l1)))
        b = int("".join(getReverse(l2)))
        print(a+b)
        return breakDown(a + b)
