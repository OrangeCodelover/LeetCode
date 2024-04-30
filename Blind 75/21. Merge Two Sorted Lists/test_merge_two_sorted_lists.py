import unittest
from typing import Optional

from merge_two_sorted_lists import Solution, ListNode

def print_list(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

class TestSolution(unittest.TestCase):
    def test_mergeTwoLists(self):
        # Creating two sorted linked lists
        list1 = ListNode(1)
        list1.next = ListNode(3)
        list1.next.next = ListNode(5)

        list2 = ListNode(2)
        list2.next = ListNode(4)
        list2.next.next = ListNode(6)

        # Merging the lists
        solution = Solution()
        merged_list = solution.mergeTwoLists(list1, list2)

        # Asserting the merged list
        expected_output = [1, 2, 3, 4, 5, 6]
        actual_output = []
        while merged_list:
            actual_output.append(merged_list.val)
            merged_list = merged_list.next
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
