class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = list()
        for index in range(len(nums)):
            item = 1
            while index - 1 >= 0:
                item *= nums[index - 1]
                index -= 1
            prefix.append(item)

        suffix = list()
        for index in range(len(nums)):
            item = 1
            while index + 1 < len(nums):
                item *= nums[index + 1]
                index += 1
            suffix.append(item)
        
        print(prefix)

        return [a * b for a, b in zip(prefix, suffix)]
        