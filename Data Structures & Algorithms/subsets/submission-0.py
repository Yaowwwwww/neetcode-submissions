class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(choiceList,track,result):
            result.append(track[:])
            for i in range(len(choiceList)):
                choice = choiceList[i]
                track.append(choice)
                nextC = choiceList[i + 1:]
                backtrack(nextC,track,result)
                track.pop()
            
        track = []
        result = []
        backtrack(nums,track,result)

        return result
            
