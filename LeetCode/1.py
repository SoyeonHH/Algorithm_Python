class Solution:
    # Brute-Force => O(n^2)
    def twoSum_BruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


    # target-n in => O(n)
    def twoSum_in(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if target-n in nums[i+1:]:
                return [i, nums[i+1:].index(target-n) + (i+1)]


    # 딕셔너리 활용 => 분할 상환 분석 O(1)
    def twoSum_key(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # key, value 바꿔서 딕셔너리 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]


    # Brute-Force를 하나의 for문으로 개선
    def twoSum_1for(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i