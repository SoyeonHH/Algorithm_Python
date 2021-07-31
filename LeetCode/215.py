import heapq

class Solution:
    def findKthLargest_heapify(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    def findKthLargest_nlargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_timsort(self, nums: list[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]