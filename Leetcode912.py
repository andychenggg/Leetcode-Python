from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1, [i for i in nums])
        return nums

    def mergeSort(self, nums: List[int], start: int, end: int, tmp: list[int]) -> None:
        '''
        Merge sort:
        time complexity: O(nlogn)
        space complexity: O(n)
        '''
        if start >= end:
            return
        
        mid = (start + end)//2
        
        self.mergeSort(nums, start, mid, tmp)
        self.mergeSort(nums, mid+1, end, tmp)

        self.merge(nums, start, mid, end, tmp)

    def merge(self, nums: List[int], start: int, mid: int, end: int, tmp: list[int]) -> None:
        left = start
        right = mid+1
        p = start

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                tmp[p] = nums[left]
                p += 1
                left += 1
            else:
                tmp[p] = nums[right]
                p += 1
                right += 1

        while left <= mid:
            tmp[p] = nums[left]
            p += 1
            left += 1

        while right <= end:
            tmp[p] = nums[right]
            p += 1
            right += 1
        
        p = start
        while p <= end:
            nums[p] = tmp[p]
            p += 1
        
