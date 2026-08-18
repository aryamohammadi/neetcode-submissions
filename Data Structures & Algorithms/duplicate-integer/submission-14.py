class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCheck = set()
        for num in range(len(nums)):
            if nums[num] in numsCheck:
                return True
            numsCheck.add(nums[num])
        return False