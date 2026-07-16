class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        def backtrack(i, curr):
            #base case
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            #处理左边(include)(需要回来)
            backtrack(i + 1, curr)
            curr.pop()

            #处理右边（dont include）（不用回来，因为左边已经回溯了）
            #跳过逻辑
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)

        backtrack(0, [])
        return res
            
