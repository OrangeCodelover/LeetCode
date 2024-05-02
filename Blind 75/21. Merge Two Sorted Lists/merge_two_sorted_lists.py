from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        merge_list = dummy
        while (list1 is not None) or (list2 is not None):
            if list1 is None:
                merge_list.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                merge_list.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val > list2.val:
                merge_list.next = ListNode(list2.val)
                list2 = list2.next
            elif list1.val < list2.val or list2 is None:
                merge_list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merge_list.next = ListNode(list1.val)                
                list1 = list1.next
                
            merge_list = merge_list.next
        return dummy.next