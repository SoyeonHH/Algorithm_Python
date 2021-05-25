
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs_1(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 head를 가리키도록 할당 (swap)
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next

    def swapPairs_2(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head