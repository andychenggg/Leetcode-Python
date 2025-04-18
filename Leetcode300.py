from typing import List
'''
CodeTop8, Leetcode300
https://leetcode.cn/problems/longest-increasing-subsequence/description/
'''

class Solution:
    '''
    dp:
    Time Complexity: O(n^2)
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    res = max(res, dp[i])
        return res
    
    '''
    Greedy+Binary Search;
    Time Complexity: O(nlog(n))
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        min_last = [1 for _ in range(len(nums)+1)]
        min_last[1] = nums[0]
        res = 1
        for i in range(len(nums)):
            if min_last[res] < nums[i]:
                res = res + 1
                min_last[res] = nums[i]
            else:
                l = 1
                r = res
                mid = 0
                while l <= r:
                    mid = (l+r) // 2
                    if min_last[mid] < nums[i]:
                        l = mid + 1
                    elif min_last[mid] == nums[i]:
                        break
                    else:
                        r = midw
                min_last[mid] = nums[i]
        return res


Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
