class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 # Counter for word1
        i2 = 0 # Counter for word2

        result_string = []

        while i < len(word1) and i2 < len(word2):
           result_string.append(word1[i])
           result_string.append(word2[i2])

           i += 1
           i2 += 1

        result_string.append(word1[i:]) # Append remainder
        result_string.append(word2[i2:]) # Append remainder

        return "".join(result_string)

    # An original albeit less efficient solution
    def altMerge(self, fword: str, sword: str) -> str:
        length = 0
        output = ''
        if len(fword) > len(sword):
            length = len(sword)
        elif len(sword) > len(fword):
            length = len(fword)
        else:
            length = len(fword)

        for i in range(length):
            output = output+fword[i]
            output = output+sword[i]

        output = output+fword[length:]
        output = output+sword[length:]

        return output
