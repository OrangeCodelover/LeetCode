from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Edge case for empty list or single-node list
        
        even_head = ListNode(0)
        odd_head = ListNode(0)
        odd = odd_head
        even = even_head
        count = 0
        current = head
        while current:
            # Even
            if count % 2 != 0:
                even.next= current
                even = even.next
            # Odd
            else:                
                odd.next = current
                odd = odd.next

            count += 1
            current = current.next

        # Ensure even list ends
        even.next = None
        # Connect odd list with even list
        odd.next = even_head.next
        
        return odd_head.next # Return head of the modified list

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

if __name__ == "__main__":
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])

    print("Original List:")
    print_linked_list(head)

    odd_even_head = solution.oddEvenList(head)
    print("Odd Even List:")
    print_linked_list(odd_even_head)