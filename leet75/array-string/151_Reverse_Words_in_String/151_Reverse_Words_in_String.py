class Solution:
    def reverseWords(self, s: str) -> str:
       s_list = s.split()

       s_reverse = s_list[::-1]

       return ' '.join(s_reverse)
