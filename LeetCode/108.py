'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

* 높이 균형(Height Balanced) 이진 트리 : 모든 노드의 두 Subtree 간 깊이 차이가 1 이하인 트리
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node
