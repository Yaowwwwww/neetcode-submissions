class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length):
            j = i + 1
            while(j < length):
                iElement, jElement = numbers[i], numbers[j]
                if iElement + jElement == target:
                    return list((i + 1 ,j + 1))
                j += 1