'''
정렬되어 있는 두 연결 리스트를 병합하라.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 반복문을 이용한 풀이
    def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = ListNode(0)
        temp = new
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return new.next

    # 재귀 구조로 연결
    def mergeTwoLists_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists_2(l1.next, l2)
        return l1