from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_intervals = sorted(intervals, key=lambda a: a[0])
        res = []
        cur = sort_intervals[0]
        for inter in sort_intervals:
            if cur[1] >= inter[0]:
                cur[1] = max(cur[1], inter[1])
            else:
                res.append(cur)
                cur = inter
        res.append(cur)
        return res
