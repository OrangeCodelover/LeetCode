import unittest
from recent_counter import RecentCounter

# Unit tests for RecentCounter
class TestRecentCounter(unittest.TestCase):
    
    def test_basic_case(self):
        counter = RecentCounter()
        self.assertEqual(counter.ping(1), 1)       # [1]
        self.assertEqual(counter.ping(100), 2)     # [1, 100]
        self.assertEqual(counter.ping(3001), 3)    # [1, 100, 3001]
        self.assertEqual(counter.ping(3002), 3)    # [100, 3001, 3002]

    def test_edge_case_with_exact_boundary(self):
        counter = RecentCounter()
        self.assertEqual(counter.ping(3000), 1)    # [3000]
        self.assertEqual(counter.ping(6000), 2)    # [3000, 6000]
        self.assertEqual(counter.ping(9000), 2)    # [6000, 9000]

    def test_case_with_sequential_pings(self):
        counter = RecentCounter()
        self.assertEqual(counter.ping(100), 1)     # [100]
        self.assertEqual(counter.ping(200), 2)     # [100, 200]
        self.assertEqual(counter.ping(300), 3)     # [100, 200, 300]
        self.assertEqual(counter.ping(3100), 4)    # [100, 200, 300, 3100]
        self.assertEqual(counter.ping(3200), 4)    # [200, 300, 3100, 3200]
        self.assertEqual(counter.ping(3300), 4)    # [300, 3100, 3200, 3300]

    def test_large_gaps_between_pings(self):
        counter = RecentCounter()
        self.assertEqual(counter.ping(1), 1)       # [1]
        self.assertEqual(counter.ping(3000), 2)    # [1, 3000]
        self.assertEqual(counter.ping(6000), 2)    # [3000, 6000]
        self.assertEqual(counter.ping(9000), 2)    # [6000, 9000]
    
    def test_multiple_calls_in_rapid_succession(self):
        counter = RecentCounter()
        self.assertEqual(counter.ping(1000), 1)    # [1000]
        self.assertEqual(counter.ping(2000), 2)    # [1000, 2000]
        self.assertEqual(counter.ping(2500), 3)    # [1000, 2000, 2500]
        self.assertEqual(counter.ping(2800), 4)    # [1000, 2000, 2500, 2800]
        self.assertEqual(counter.ping(5000), 4)    # [2000, 2500, 2800, 5000]
# Run the tests
if __name__ == "__main__":
    unittest.main()