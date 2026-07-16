class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = v + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    result.add((v, nums[l], nums[r]))
                    l += 1
                    r -= 1

                    # 跳过重复值
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return [list(triplet) for triplet in result]
