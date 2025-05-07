from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_q = deque()
        res = []
        for i in range(len(nums)):
            while len(mono_q) != 0 and mono_q[-1] < nums[i]:
                mono_q.pop()
            mono_q.append(nums[i])

            if i >= k-1:
                res.append(mono_q[0])
                if mono_q[0] == nums[i-k+1]:
                    mono_q.popleft()

        return res