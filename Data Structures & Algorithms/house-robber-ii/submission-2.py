class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] =  max(dp[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        dp2 = [0] * len(nums)
        dp2[1] = nums[1]
        dp2[2] = max(dp2[1], nums[2])
        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        return max(dp[-2], dp2[-1])

        
        
