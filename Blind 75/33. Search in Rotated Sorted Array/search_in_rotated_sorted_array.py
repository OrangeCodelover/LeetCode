from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        nums_len = len(nums)
        while i < nums_len:
            if target == nums[i]:
                return i
            elif target == nums[nums_len-i-1]:
                return nums_len-i-1
            elif target > nums[i] or target < nums[nums_len-i-1]:
                i+=1
            else:
                return -1
        return -1