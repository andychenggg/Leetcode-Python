from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1 = p2 = 0
        map = {1: 0, 0: 0}
        res = 0
        while p1 <= p2:
            while p2 <= len(nums):
                map[nums[p2]] += 1
                if map[0] <= k:
                    res = max(p2-p1+1, res)
                else:
                    break
                p2 += 1
            map[nums[p1]] -= 1
            p1 += 1
        return res