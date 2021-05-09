
class Solution:
    '''
    TimeComplexity is O(W^0.25 * logW), where W=10^18
    Y is palindrome => X=Y*Y is superpalindrome, Z is half of digit
    X range [1,10^18) => Y range [1,10^9) => Z range [1,10^5) is enough

    * reference : DBabichev (https://leetcode.com/problems/super-palindromes/discuss/1197292/Python-math-solution-explained)
    '''

    nums = []
    for i in range(1, 100000):
        cand1 = int(str(i) + str(i)[::-1])**2
        cand2 = int(str(i)[:-1] + str(i)[::-1])**2
        if str(cand1) == str(cand1)[::-1]:  nums += [cand1]
        if str(cand2) == str(cand2)[::-1]:  nums += [cand2]

    nums = sorted(nums)

    def superpalindromesInRange(self, left: str, right: str) -> int:
        for i in range(len(self.nums)):
            if self.nums[i] >= int(left):
                L = i
                break
        for j in range(L, len(self.nums)):
            if self.nums[j] > int(right):
                R = j
                break

        return R - L



sol = Solution()
result = sol.superpalindromesInRange(4, 1000)
print(result)
