from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[i] + nums[i+j+1] == target:
                return [i, i+j+1]
        
    return 0
#EX_1
nums = [2,7,11,15]
target = 9   
a = twoSum(nums,target)
print(a)
# [0,1]

#EX_2
nums = [3,2,4]
target = 6   
b = twoSum(nums,target)
print(b)
# [1,2]

#EX_3
nums = [3,3]
target = 6   
c = twoSum(nums,target)
print(c)
# [0,1]