class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        Min = float("inf")


        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            m = (l + r) // 2
            # print(m)
            if nums[m] < Min:
                Min = nums[m]
            if nums[l] <= nums[m]:#m in left sorted
                l = m + 1
            else: #m in right sorted
                r = m

        return Min
            