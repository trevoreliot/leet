class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def is_divisor(s):
            if len1 % s or len2 % s:
                return False
            f1 = len1 // s
            f2 = len2 // s
            str1[:s] * f1 == str1 and str1[:s] * f2 == str2

        for s in range(min(len1, len2), 0, -1):
            if is_divisor(str1[:s]):
                return str1

            return ""


# Original but less efficient solution
    def gcd_of_strings(self, str1: str, str2: str) -> str:
