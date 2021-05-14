class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 자기 자신을 제외한 왼쪽 곱셈 배열
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 배열에 자기 자신을 제외한 오른쪽 값을 차례대로 곱함
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out