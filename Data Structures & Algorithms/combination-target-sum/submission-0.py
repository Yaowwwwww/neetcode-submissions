class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            if sum(curr) == target:
                result.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            newElement = nums[i]
            curr.append(newElement)
            #left branch
            dfs(i, curr, total + newElement)

            # pop
            curr.pop()
            #right branch
            dfs(i + 1, curr, total)


        dfs(0, [], 0)
        return result