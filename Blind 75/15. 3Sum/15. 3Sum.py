from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    # print("num:", nums)
    sum_zero = []
    for i,n in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        # print("i:",i)
        j = i + 1
        k = len(nums) -1
        # print("k_1 :",k)
        while j < k:
            # print("j :",j)
            # print("k :",k)
            if   n + nums[j] + nums[k] == 0:
                sum_zero.append([n,nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                k -= 1
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
