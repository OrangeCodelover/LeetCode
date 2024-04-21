from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    # print("num:", nums)
    sum_zero = []
    for i,n in enumerate(nums):
        # print("i:",i)
        j = i + 1
        k = len(nums) -1
        # print("k_1 :",k)
        while j < k:
            # print("j :",j)
            # print("k :",k)
            if   n + nums[j] + nums[k] == 0:
                newArray = [n,nums[j], nums[k]]
                if newArray not in sum_zero:
                    sum_zero.append(newArray) 
                j += 1
            elif n + nums[j] + nums[k] < 0:
                j += 1
            elif n + nums[j] + nums[k] > 0:
                k -= 1
                
    return sum_zero

#EX_1
nums = [-1,0,1,2,-1,-4]
a = threeSum(nums)
print(a)
# [[-1,0,1],[-1,-1,2]]

#EX_2
nums = [0,1,1]
a = threeSum(nums)
print(a)
# []

#EX_1
nums = [0,0,0]
a = threeSum(nums)
print(a)
# [[0,0,0]]

"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_zero = []
        nums.sort()  # Sort the input list
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    sum_zero.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return sum_zero

"""