class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arya = set()
        for i in nums:
            if i in arya:
                return True
            arya.add(i)
        return False