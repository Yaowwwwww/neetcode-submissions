class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
        digits_map = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mon","7":"pqrs","8":"tuv","9":"wxyz"}

        def dfs(i, layer):
            if i == len(digits):
                res.append("".join(layer))
                return
            first_str = digits_map[digits[i]]
            for c in first_str:
                layer.append(c)
                dfs(i + 1,layer)
                layer.pop()
                continue

        dfs(0,[])
        return res
        