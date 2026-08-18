class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for character in range(0, (len(s))//2):
            temp = s[character]
            s[character] = s[len(s) - 1 - character]
            s[len(s) - 1 - character] = temp
        