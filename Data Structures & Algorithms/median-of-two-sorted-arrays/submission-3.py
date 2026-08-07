class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)

        totalLeft = (l1 + l2 + 1) // 2

        leftForCut1 = 0
        rightForCut1 = l1

        while leftForCut1 <= rightForCut1:
            #定义cut1,2 和ABCD
            cut1 = (leftForCut1 + rightForCut1) // 2
            A = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            B = nums1[cut1] if cut1 < l1 else float('inf')

            cut2 = totalLeft - cut1
            C = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            D = nums2[cut2] if cut2 < l2 else float('inf')

            # A|B 1|2
            # C|D 7|8
            #if cut1太右边
            if A > D:
                rightForCut1 = cut1 - 1
            #elif cut1太左边
            elif C > B:
                leftForCut1 = cut1 + 1
            #else 切对了
            else:
                if (l1 + l2) % 2 == 1:
                    median = max(A,C)
                else:
                    median = (max(A, C) + min(B, D)) / 2

                return median
