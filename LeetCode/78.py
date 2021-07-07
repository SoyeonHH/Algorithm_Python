class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            # 경로를 만들면서 dfs
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result