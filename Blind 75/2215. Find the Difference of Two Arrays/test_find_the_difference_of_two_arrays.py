import unittest

from find_the_difference_of_two_arrays import Solution

class testFindDifference(unittest.TestCase):
    def test_sample_1(self):
        nums1 = [1,2,3]
        nums2 = [2,4,6]
        expected = [[1,3],[4,6]]
        solution_instance = Solution()
        output = solution_instance.findDifference(nums1,nums2)
        self.assertEqual(output, expected)
    
    def test_sample_2(self):
        nums1 = [1,2,3,3]
        nums2 = [1,1,2,2]
        expected = [[3],[]]
        solution_instance = Solution()
        output = solution_instance.findDifference(nums1,nums2)
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()