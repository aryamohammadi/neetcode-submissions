class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listNums = set()
        for num in nums:
            if num in listNums:
                return True
            listNums.add(num)
        return False