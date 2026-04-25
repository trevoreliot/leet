class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        candy_mizer = max(candies)
        candy_ranker = []

        for i in candies:
            if i + extraCandies >= candy_mizer:
                candy_ranker.append(True)
            else:
                candy_ranker.append(False)

        return candy_ranker
