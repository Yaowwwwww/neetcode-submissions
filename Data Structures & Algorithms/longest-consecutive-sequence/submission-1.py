class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        #记录array开始
        starts = [num for num in nums if num - 1 not in nums]

        #根据每个开始构建hashset，然后如果存在+1就加入 直到没有
        lengths = [0]
        for start in starts:
            cnt = 1
            while(start + 1 in nums):
                cnt += 1
                start += 1
            lengths.append(cnt) 
        return max(lengths)