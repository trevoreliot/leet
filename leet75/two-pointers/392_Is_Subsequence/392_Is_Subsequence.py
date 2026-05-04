class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        text = list(t)
        accum = 0
        target = len(s)

        if s == "":
            return True

        for n in text:
            if n == s[accum]:
                accum += 1

            if accum == target:
                return True

        return False
