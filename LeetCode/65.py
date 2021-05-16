'''
Problem : 65. Valid Number
Solution Reference : https://leetcode.com/problems/valid-number/discuss/1209315/JS-Python-Java-C%2B%2B-or-Easy-Character-Conditional-Solution-w-Explanation
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        num, exp, sign, dec = False, False, False, False
        # 한 문자씩 판단
        for c in s:
            if c >= '0' and c <= '9': num = True
            elif c == 'e' or c == 'E':
                if exp or not num: return False
                else: exp, num, sign, dec = True, False, False, False
            elif c == '+' or c == '-':
                if sign or num or dec: return False
                else: sign = True
            elif c == '.':
                if dec or exp: return False
                else: dec = True
            else: return False
        return num