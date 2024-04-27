from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_list = ListNode(0)
        while (list1 is not None) or (list2 is not None):
            if list1 is None:
                merge_list.next = ListNode(list2.val)
                list2 = list2.next
            elif list1 is None:
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
                merge_list.next = ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next
            merge_list = merge_list.next
        return merge_list
        
    #EX_1
list1 = [1,2,4]
list2 = [1,3,4]
a = mergeTwoLists(self, list1, list2)
print(a)


        