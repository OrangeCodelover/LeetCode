from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        for i in range(len(nums)-k +1):
            sum = 0
            for j in range(k):
                sum += nums[i+j]
            if i == 0:
                max_sum = sum           
            max_sum = max(sum, max_sum)
            print("max",max_sum)
        return float(max_sum/k)
    

# Main function to run the class
if __name__ == "__main__":
    solution = Solution()

    # nums = [1,12,-5,-6,50,3]
    # k = 4
    nums = [-1]
    k = 1
    solution.findMaxAverage(nums, k)

#With Brute Force Approach