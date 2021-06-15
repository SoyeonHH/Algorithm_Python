import collections

class Solution:
    def numJewelsInStones_1(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # 돌(S)의 빈도 수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석(J)의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

    def numJewelsInStones_2(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)    # 키 존재 여부를 매번 판별할 필요 X
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count

    def numJewelsInStones_3(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)  # 돌(S) 빈도 수 계산, defaultdict와 마찬가지로 존재하지 않는 키에 대한 예외처리 필요가 없음.
        count = 0

        for char in jewels:
            count += freqs[char]

        return count

    # Pythonic Way (리스트 컴프리헨션)
    def numJewelsInStones_4(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
