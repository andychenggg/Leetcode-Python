from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for i in prices:
            if i - lowest > res:
                res = i - lowest
            
            if i < lowest:
                lowest = i
        
        return res