class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Map1 = [0 for i in range(26)]
        Map2 = [0 for i in range(26)]

        for char in s:
            Map1[ord(char) - ord('a')] +=1
        for char in t:
            Map2[ord(char)-ord('a')] += 1
        return Map1 == Map2