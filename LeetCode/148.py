'''
LeetCode 148. Sort List

연결리스트를 O(n log n)에 정렬하라.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList_mergeSort(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # Runner
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None  # 연결 리스트 끊기

        # Divide Reference
        l1 = self.sortList_mergeSort(head)
        l2 = self.sortList_mergeSort(slow)

        return self.mergeTwoLists(l1, l2)


    def sortList_Pythonic(self, head: ListNode) -> ListNode:

        # Linked List -> Python List
        p = head
        lst: list = []
        while p:
            lst.append(p.val)
            p = p.next

        # sort
        lst.sort()

        # Python List -> Linked List
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head