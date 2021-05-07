import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # alphanumeric을 제외한 문자 정규필터링
        s = re.sub('[^a-z0-9]','',s)

        return s==s[::-1]  # 슬라이싱으로 문자열 뒤집기

instance = Solution()
s = "A man, a plan, a canal: Panama"
print(Solution.isPalindrome(instance, s))
