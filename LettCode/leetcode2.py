#!/usr/bin/python3


from typing import List
from decimal import *


class Solution:
    def findMedianSortedArrays(self, 
        nums1: List[int], 
        nums2: List[int]) -> float:

        nums = sorted(nums1+nums2)
        print(f"nums {nums}")
        if len(nums) % 2 == 0:
            return float(nums[(len(nums)//2)-1] + nums[len(nums)//2])/2
        else:
            return float(nums[len(nums)//2])


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([3], [-2, -1]))
