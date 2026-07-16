class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()#inplace sort without using extra memory
        result = []
        def dfs(i, curr, total):
            #Base Case
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            #Two Branch Recursive Call
            num = candidates[i]
            curr.append(num)
            dfs(i + 1, curr, total + num)
            curr.pop()

            #✅ 回溯逻辑就是：
            # 先加这个数（即使是重复的），试试看能不能组成目标 → 这是合法路径的一部分

            # **撤销（pop）**当前这条路径

            # 然后跳过后续所有值相同的“兄弟”分支，避免重复解
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return result
