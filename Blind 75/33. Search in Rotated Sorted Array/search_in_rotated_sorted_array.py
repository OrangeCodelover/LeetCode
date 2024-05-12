from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums(0) == target:
            return 0
        i = 1
        while i < len(nums):
            if target == nums(i):
                return i
            elif target == nums(-i):
                return len(nums) - i
            elif target > nums(i) and target < nums(-i):
                i+=1
            else:
                return -1

