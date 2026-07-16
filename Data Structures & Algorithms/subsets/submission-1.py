class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, path):
            if i == len(nums) + 1:
                return
            res.append(path[:])
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j + 1, path)
                path.pop()
        dfs(0,[])
        return res
        
            
