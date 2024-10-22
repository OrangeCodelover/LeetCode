from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        # print("Set1", nums1)
        

        nums1_unik = list(nums1 - nums2)
        nums2_unik = list(nums2 - nums1)

        
        # print ("nums1:", nums1_unik)
        # print ("nums2:", nums2_unik)

        return [nums1_unik, nums2_unik]

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    solution.findDifference(nums1, nums2)