import collections

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        sorted_str = ""

        for c in order:
            for _ in range(collections.Counter(str)[c]):
                sorted_str += c
                str = str.replace(c, "")  # replace : 반복 당 하나의 문자 제거 가능

        sorted_str += str

        return sorted_str