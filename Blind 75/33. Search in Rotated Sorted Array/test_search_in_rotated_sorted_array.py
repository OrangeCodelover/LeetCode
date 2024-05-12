import unittest
# delete _pycache_
import shutil
import os

from search_in_rotated_sorted_array import Solution
    
class TestSearch(unittest.TestCase):

    def test_search_exists(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        solution_instance = Solution()
        self.assertEqual(solution_instance.search(nums, target), 4)

    def test_search_not_exists(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        solution_instance = Solution()
        self.assertEqual(solution_instance.search(nums, target), -1)

    def test_single_element_array(self):
        nums = [1]
        target = 0
        solution_instance = Solution()
        self.assertEqual(solution_instance.search(nums, target), -1)
    
    def test_search_not_exists_2(self):
        nums = [1,3]
        target = 0
        solution_instance = Solution()
        self.assertEqual(solution_instance.search(nums, target), -1)



if __name__ == "__main__":
    unittest.main()


# Cleanup _pycache_ directory
shutil.rmtree("__pycache__", ignore_errors=True)