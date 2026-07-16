class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # m in left sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:#l小于m值，并且目标大于m或者目标小于l 因此搜索右手
                    l = m + 1
                else:# 否则搜索左手
                    r = m - 1

            # m in right sorted
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
