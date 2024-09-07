import unittest
import shutil
import os

from move_zeros import Solution

class TestMoveZeros(unittest.TestCase):
    def test_move_to_the_end(self):
        nums = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        solution_instance = Solution()
        solution_instance.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_empty(self):
        nums = [0]
        expected = [0]
        solution_instance = Solution()
        solution_instance.moveZeroes(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()

    shutil.rmtree("__pycache__", ignore_errors=True)
