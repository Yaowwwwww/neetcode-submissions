class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = deque() 
        
        for i in range(n):#遍历nums
            while q and nums[i] >= nums[q[-1]]:#如果新来的数字更大，就pop q直到形成降序这样q[0]保证是窗口的最大
                q.pop()
            q.append(i)#append到队尾
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
                