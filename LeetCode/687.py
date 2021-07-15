# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # DFS recursive search to nonexistent node
            left = dfs(node.left)
            right = dfs(node.right)

            # Add 1 distance if current node and child nodes are the same
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # The result is the maximum sum of the distances between the left and right chile nodes
            self.result = max(self.result, left + right)

            # return the max of child nodes
            return max(left, right)

        dfs(root)
        return self.result