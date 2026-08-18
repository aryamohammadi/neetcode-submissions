class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numList = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in numList:
                return [numList[diff], i]
            numList[num] = i
