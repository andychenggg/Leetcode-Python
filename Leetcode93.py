from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ## index means insert a dot after it
        
        res = []
        for i in range(12):
            if i >= len(s) - 3 or i >= 3:
                break
            if i < len(s)-10 or not self.isValid(s[0:i+1]):
                # 000_000_000_000
                continue
            part1 = s[0:i+1]
            for j in range(i+1, 12):
                if j >= len(s) - 2 or j >= i+4:
                    break
                if j < len(s)-7 or not self.isValid(s[i+1:j+1]):
                    # 000_000_000_000
                    continue
                part2 = s[i+1:j+1]
                for k in range(j+1, 12):
                    if k >= len(s) - 1 or k >= j+4:
                        break
                    if k < len(s)-4 or not self.isValid(s[j+1:k+1]) or not self.isValid(s[k+1:]):
                        # 000_000_000_000
                        continue
                    res.append(part1+'.'+part2+'.'+s[j+1:k+1]+'.'+s[k+1:])

        return res


    def isValid(self, s: str) -> bool:
        val = int(s)
        if 100 <= val <= 255:
            return True
        if 10 <= val <= 99:
            return len(s) == 2
        if 0 <= val <=9:
            return len(s) == 1
            


print(Solution().restoreIpAddresses("25525511135"))