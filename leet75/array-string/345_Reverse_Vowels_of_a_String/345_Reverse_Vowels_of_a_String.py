class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u']
        listified_string = list(s)
        left_point = 0
        right_point = len(s) - 1

        while left_point < right_point:
           if s[left_point].lower() not in vowels:
               left_point += 1
           elif s[right_point].lower() not in vowels:
               right_point -= 1

           else:
               listified_string[left_point], listified_string[right_point] = listified_string[right_point], listified_string[left_point]

               left_point += 1
               right_point -= 1

        return ''.join(listified_string)
