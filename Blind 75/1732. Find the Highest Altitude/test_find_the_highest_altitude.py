import unittest

from find_the_highest_altitude import Solution

class testFindTheHighestAltitude(unittest.TestCase):
    def test_case_1(self):
        gain = [-5,1,5,0,-7]
        expected = 1
        solution_instance = Solution()
        output = solution_instance.largestAltitude(gain)
        self.assertEqual(output,expected)

if __name__ =="__main__":
    unittest.main()
