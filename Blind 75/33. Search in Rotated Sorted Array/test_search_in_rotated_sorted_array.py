import unittest
# delete _pycache_
import shutil
import os

from search_in_rotated_sorted_array import search
    
class TestSearch(unittest.TestCase):
    def test_search_exists(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(search(nums, target), 4)



if __name__ == "__main__":
    unittest.main()

# Cleanup _pycache_ directory

shutil.rmtree("__pycache__", ignore_errors = True)