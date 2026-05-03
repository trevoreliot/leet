class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


    def janky_compress(self, chars: list[str]) -> int:

        s = ""
        s1 = ""
        n_old = ""
        i = 0
        last_ind = len(chars) - 1

        for ind, n in enumerate(chars):
            if n != s1:
                n_old = n
                if i > 1:
                    chars[ind] = (str(i) + n_old)
                else:
                    chars[ind] = n_old
                i = 1
                s1 = n
            elif n == s1:
                i += 1
                chars[ind] = "delete"
            if ind == last_ind:
                if i > 1:
                    chars[ind] = str(i)

        chars = [x for x in chars if x != 'delete']

        return len(''.join(chars))
