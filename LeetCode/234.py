# Definition for singly-linked list.
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 리스트를 이용한 풀이 => 첫 번째 값 꺼내올 때 O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        if not head:
            return True

        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판볗
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    # 데크를 이용한 풀이 => 첫 번째 값 꺼내올 때 O(1)
    def isPalindrome_Deque(self, head: ListNode) -> bool:
        q = collections.deque()
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # 런너를 이용한 연결리스트 풀이
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

instance = Solution()
head : ListNode = [1,2,2,1]
print(Solution.isPalindrome_Deque(instance, head))
