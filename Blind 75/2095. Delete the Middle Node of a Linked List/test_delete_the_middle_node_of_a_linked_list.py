import unittest
from delete_the_middle_node_of_a_linked_list import Solution, create_linked_list
class TestReverseList (unittest.TestCase):

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
        modified_head = solution.deleteMiddle(head)
        expected_head = create_linked_list([1, 2, 4, 5])
        
        # Check if the reversed list equals the expected list
        self.assertTrue(self.linked_lists_are_equal(modified_head, expected_head))

    def test_1_node(self):
        head = create_linked_list([1])
        solution = Solution()
        modified_head = solution.deleteMiddle(head)
        expected_head = create_linked_list([])
        
        # Check if the reversed list equals the expected list
        self.assertTrue(self.linked_lists_are_equal(modified_head, expected_head))


# Run the tests
if __name__ == "__main__":
    unittest.main()