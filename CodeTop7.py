from typing import List

'''
codetop7, leetcode53:
https://leetcode.cn/problems/maximum-subarray/
'''
'''
use dp
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1, len(nums)):
            nums[i] = nums[i] if nums[i-1] < 0 else nums[i-1]+nums[i]

        max = nums[0]
        for i in nums:
            if i > max:
                max = i
        
        return max
    
'''
use divide-and-conquer
'''
class Info:
    def __init__(self, lms: int, rms: int, ms: int, sum: int):
        self.lms: int = lms
        self.rms: int = rms
        self.ms: int = ms
        self.sum: int = sum


class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.getInfo(nums, 0, len(nums)-1).ms

    def getInfo(self, nums: List[int], l: int, r: int) -> Info:
        if l == r:
            return Info(nums[l],nums[l],nums[l],nums[l])
        
        mid = (l+r)//2
        l_info = self.getInfo(nums, l, mid)
        r_info = self.getInfo(nums, mid+1, r)

        # merge the info
        sum = l_info.sum+r_info.sum
        lms = max(l_info.lms, l_info.sum+r_info.lms)
        rms = max(l_info.rms+r_info.sum, r_info.rms)
        ms = max(max(l_info.ms, r_info.ms), l_info.rms+r_info.lms)
        return Info(lms, rms, ms, sum)