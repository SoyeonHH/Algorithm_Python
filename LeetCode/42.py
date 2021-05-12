class Solution:
    def trap(self, height: List[int]) -> int:
        # 문제 조건 잘 보기! height.length >= 0 미리 예외처리
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), \
                                  max(height[right], right_max)

            # idea : 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume