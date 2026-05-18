from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Count the frequency of each number: e.g., {1: 1, 5: 1, 4: 2}
        counts = Counter(nums)
        output = 0

        for num in counts:
            x = k - num

            if x in counts:
                if x == num:
                    # If the matching number is itself (e.g. k=6, num=3),
                    # you can form pairs equal to half of its count
                    output += counts[num] // 2
                elif x > num:
                    # 'x > num' ensures we only count the pair (num, x) once
                    # and don't double-count it later as (x, num)
                    pairs = min(counts[num], counts[x])
                    output += pairs

        return output

    def maxOperations_slow(self, nums: list[int], k: int) -> int:

        lookup = nums[:]
        output = 0
        for num in nums:
            x = k-num
            if x in lookup and num in lookup:
                if x == num and lookup.count(x) < 2:
                    continue

                lookup.remove(x)
                lookup.remove(num)
                output += 1

        return output
