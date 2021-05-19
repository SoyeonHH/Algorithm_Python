# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 재귀 구조로 뒤집기
    def reverseList_1(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head, None)

    # 반복문으로 뒤집기
    def reverseList_2(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev