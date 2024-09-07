import unittest
# delete _pycache_
import shutil
import os

from merge_strings_alternately import Solution
    
class TestMergeStringsAlternately(unittest.TestCase):

    def test_merge_with_same_length(self):
        word1 = "abc"
        word2 = "pqr"
        merged = "apbqcr"
        solution_instance = Solution()
        self.assertEqual(solution_instance.mergeAlternately(word1, word2), merged)

    def test_merge_with_longer_word2(self):
        word1 = "ab"
        word2 = "pqrs"
        merged = "apbqrs"
        solution_instance = Solution()
        self.assertEqual(solution_instance.mergeAlternately(word1, word2), merged)

    def test_merge_with_longer_word1(self):
        word1 = "abcd"
        word2 = "pq"
        merged = "apbqcd"
        solution_instance = Solution()
        self.assertEqual(solution_instance.mergeAlternately(word1, word2), merged)

if __name__ == "__main__":
    unittest.main()

    # Cleanup _pycache_ directory
    shutil.rmtree("__pycache__", ignore_errors=True)