class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, path):
            # base case: 考虑完所有数字
            if i == len(nums):
                res.append(path[:])
                return
            
            # 选择当前 nums[i]
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            
            # 不选择当前 nums[i]
            dfs(i+1, path)
        
        dfs(0, [])
        return res
