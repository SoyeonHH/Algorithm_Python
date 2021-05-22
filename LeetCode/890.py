'''
reference : https://leetcode.com/problems/find-and-replace-pattern/discuss/1221115/JavaPython-Normalize-Words-Clean-and-Concise
'''

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def Normalize(s):
            seen = dict()
            next = "a"
            ans = ""
            for c in s:
                if c not in seen:
                    seen[c] = next
                    next = chr(ord(next) + 1)
                ans += seen[c]
            return ans

        p = Normalize(pattern)
        ans = []
        for word in words:
            if Normalize(word) == p:
                ans.append(word)
        return ans