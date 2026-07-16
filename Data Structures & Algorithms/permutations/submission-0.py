class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])

        toAdd = nums[0]

        result = []

        for p in perms:
            for i in range(len(p) + 1):
                newlist = p[:]
                newlist.insert(i, toAdd)
                result.append(newlist)

        return result