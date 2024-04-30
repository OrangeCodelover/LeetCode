from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next
    return dummy


#EX_1
 
head = [1,2,3,4,5]
n = 2 
a = removeNthFromEnd(head,n)
# print(a)
# # [1,2,3,5]

