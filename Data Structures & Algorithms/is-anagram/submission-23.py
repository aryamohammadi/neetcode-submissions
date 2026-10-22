class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCountS = {}
        charCountT = {}
        for char in s:
            charCountS[char] = charCountS.get(char, 0) + 1
        for char in t:
            charCountT[char] = charCountT.get(char, 0) + 1
        if charCountS == charCountT:
            return True
        return False



        