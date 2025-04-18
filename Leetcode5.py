class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=="":
            return ""
        
        maxLen = 1
        resL = 0

        palindrome = [[False for _ in s] for _ in s]

        for i in range(len(s)):
            for j in range(len(s)):
                if j + i >= len(s):
                    continue

                if i <= 2:
                    palindrome[j][j+i] = s[j] == s[j+i]
                else:
                    palindrome[j][j+i] = s[j] == s[j+i] and palindrome[j+1][j+i-1]
                
                if palindrome[j][j+i] and i+1 > maxLen:
                    maxLen = i+1
                    resL = j
                
        return s[resL:resL+maxLen]

print(Solution().longestPalindrome("cbbd"))
