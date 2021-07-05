import itertools

class Solution:
    def combine_1(self, n: int, k: int) -> list[list[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    def combine_2(self, n: int, k: int) -> list[list[int]]:
        return list(itertools.combinations(range(1, n + 1), k))