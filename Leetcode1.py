from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p0, p1 = 0, len(nums)-1
        nums_index = enumerate(nums)
        nums_index = sorted(nums_index, key=lambda x:x[1])

        while p0 < p1:
            if nums_index[p0][1] + nums_index[p1][1] == target:
                return [nums_index[p0][0], nums_index[p1][0]]
            elif nums_index[p0][1] + nums_index[p1][1] > target:
                p1 -=1
            else:
                p0+=1
        