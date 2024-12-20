from typing import List

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         for i in range(len(nums)-k +1):
#             sum = 0
#             for j in range(k):
#                 sum += nums[i+j]
#             if i == 0:
#                 max_sum = sum           
#             max_sum = max(sum, max_sum)
#             print("max",max_sum)
#         return float(max_sum/k)
    

# # Main function to run the class
# if __name__ == "__main__":
#     solution = Solution()

#     # nums = [1,12,-5,-6,50,3]
#     # k = 4
#     nums = [-1]
#     k = 1
#     solution.findMaxAverage(nums, k)

#Above With Brute Force Approach

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sum of the first group of k
        temp_sum = sum(nums[:k])
        max_sum = temp_sum
        print("firsrt Mmax",max_sum)
        if k > 1:
            for i in range(len(nums)-k):
                temp_sum = temp_sum - nums[i] + nums[i+k]
                print("temP:",temp_sum)
                max_sum = max(max_sum,temp_sum)
                print("finnal max",max_sum)
            return float(max_sum/k)
        else:
            return max(nums)  

# Main function to run the class
if __name__ == "__main__":
    solution = Solution()

    # nums = [1,12,-5,-6,50,3]
    # k = 4
    # nums = [-1]
    # k = 1
    # nums = [0,4,0,3,2]
    # k = 1
    nums = [4,2,1,3,3]
    k = 2
    solution.findMaxAverage(nums, k)
