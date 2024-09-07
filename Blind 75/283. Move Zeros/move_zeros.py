from typing import List
# nums = [0,1,0,3,12]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeros = 0
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)


# moveZeroes(nums)
# print(nums)
