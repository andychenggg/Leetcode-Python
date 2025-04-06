class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        CodeTop1, Leetcode3: https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
        '''
        charSet = set()
        p1 = p2 = 0
        resLen = 0
        while p2 < len(s):
            while p2 < len(s) and s[p2] not in charSet:
                charSet.add(s[p2])
                p2 = p2 +1
            resLen = resLen if resLen > len(charSet) else len(charSet)

            charSet.remove(s[p1])
            p1 = p1 + 1
            if p2 < p1:
                p2 = p1
        return resLen

    