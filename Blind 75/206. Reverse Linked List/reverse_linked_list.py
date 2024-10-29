from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Find the length of the node
        # count = 0
        # current = head
        # while current:
        #     count +=1
        #     current = current.next
        # return count
        prev = None
        current = head
        while current:

            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

      

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

    reversed_head = solution.reverseList(head)
    print("Reversed List:")
    print_linked_list(reversed_head)