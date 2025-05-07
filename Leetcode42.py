from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max =  [0 for _ in height], [0 for _ in height]
        res = 0

        max_h = 0
        for i in range(len(height)):
            max_h = l_max[i] = max(height[i], max_h)
            print(i, ' ', l_max[i])

        max_h = 0
        for i in range(len(height))[::-1]:
            max_h = r_max[i] = max(height[i], max_h)
        
        for i in range(len(height)):
            res += min(r_max[i], l_max[i]) - height[i]

        return res
