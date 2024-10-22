import unittest

from removing_stars_from_a_string import Solution

class removeStars(unittest.TestCase):
    def test_sample_1(self):
        s = "leet**cod*e"
        expected = "lecoe"
        solution_instance = Solution()
        output = solution_instance.removeStars(s)
        self.assertEqual(output, expected)
    
    def test_sample_2(self):
        s = "erase*****"
        expected = ""
        solution_instance = Solution()
        output = solution_instance.removeStars(s)
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()