class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array of two nums, also target
        # target - nums i = nums j
        # return i and j
        mp = {}
        for i in range (len(nums)):
            if target - nums[i] in mp:
                j = mp[target - nums[i]]
                return [j, i]
            mp[nums[i]] = i