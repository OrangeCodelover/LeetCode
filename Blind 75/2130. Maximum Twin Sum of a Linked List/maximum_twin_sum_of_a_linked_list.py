from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None
        if head == None:
            return 0
        # Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Make second half a reverse linked list
        prev = None
        current = slow

        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        first_half = head
        second_half = prev

        pair_sum = first_half.val + second_half.val
        while second_half:
            updated_sum = first_half.val + second_half.val
            if pair_sum < updated_sum:
                pair_sum = first_half.val + second_half.val
            
            second_half = second_half.next
            first_half = first_half.next
        
        return pair_sum

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
    head = create_linked_list([5, 4, 2, 1])

    print("Original List:")
    print_linked_list(head)

    pair_sum = solution.pairSum(head)
    print("Pair Sum:", pair_sum)