class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        half = len(nums) // 2

        index = 0
        
        if target not in nums:
                return -1

        while len(nums) > 1:
            if target not in nums:
                return -1
            if target == nums[half]:
                return index + half
            elif target < nums[half]:
                right = half
                nums = nums[left:half]
                half = len(nums) // 2
            elif target > nums[half]:
                index += half
                print(half)
                left = half
                nums = nums[half:right]
                print(nums)
                half = len(nums) // 2
                print(half)
        return index
                