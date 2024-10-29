from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Find the length of the node
        count = 0
        current = head
        while current:
            count+=1
            current = current.next

        if count< 2:
            return None
        # Find the middle one
        mid = count//2

        # Delete
        prev = None
        current = head
        for i in range(mid):
            prev = current
            current = current.next
        prev.next = current.next

        return head


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

    delete_middle_head = solution.deleteMiddle(head)
    print("Modified List:")
    print_linked_list(delete_middle_head)