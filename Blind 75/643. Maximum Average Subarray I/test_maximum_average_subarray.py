import unittest
import os

from maximum_average_subarray_I import Solution

class TestMaximumAverageSubarray(unittest.TestCase):
    def test_find_max_average(self):
        nums = [1,12,-5,-6,50,3]
        k = 4
        expected = 12.75000
        solution_instance = Solution()
        output = solution_instance.findMaxAverage(nums,k)
        self.assertEqual( output, expected)

    def test_one_positive_number(self):
        nums = [5]
        k = 1
        expected = 5
        solution_instance = Solution()
        output = solution_instance.findMaxAverage(nums,k)
        self.assertEqual(output, expected)

    def test_one_negative_number(self):
        nums = [-1]
        k = 1
        expected = -1
        solution_instance = Solution()
        output = solution_instance.findMaxAverage(nums,k)
        self.assertEqual(output, expected)

if __name__ =="__main__":
    unittest.main()
