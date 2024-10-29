import unittest
from reverse_linked_list import Solution, create_linked_list
class TestReverseList (unittest.TestCase):
    # Find the length
    # def test_multiple_nodes(self):
    #     head = create_linked_list([1, 2, 3, 4, 5])
    #     solution = Solution()
    #     self.assertEqual(solution.reverseList(head), 5)

    def linked_lists_are_equal(self, head1, head2):
        """Helper function to check if two linked lists are equal."""
        current1, current2 = head1, head2
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None  # Both should be None at the end

    def test_basic(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        solution = Solution()
        reversed_head = solution.reverseList(head)
        expected_head = create_linked_list([5, 4, 3, 2, 1])
        
        # Check if the reversed list equals the expected list
        self.assertTrue(self.linked_lists_are_equal(reversed_head, expected_head))


# Run the tests
if __name__ == "__main__":
    unittest.main()