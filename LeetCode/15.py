class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 투 포인터
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:    # 정답인 경우 result에 추가
                    result.append([nums[i], nums[left], nums[right]])
                    # 계속 진행 (중복값 건너뛰기)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif sum > 0:
                    right -= 1
                else:
                    left += 1

        return result
