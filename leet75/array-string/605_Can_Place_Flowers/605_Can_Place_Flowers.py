class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f)-1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        return n <= 0 # returning a bool from logic operator instead of variable


    # Original non-optimal solution (really bad lol)
    def can_place_flower(self, flowerbed: list[int], n: int) -> bool:

        flower_output = False
        spots_available = 0
        lead = 1
        lag = -1

        if len(flowerbed) <= 2:
            if sum(flowerbed) == 0:
                spots_available = 1
            if n <= spots_available:
                flower_output = True


            return flower_output

        for index, value in enumerate(flowerbed):
            if index == 0 and value == 0 and flowerbed[lead] == 0:
                spots_available += 1
                flowerbed[index] = 1
            elif index == (len(flowerbed) - 1) and value == 0 and flowerbed[-2] == 0:
                spots_available += 1
                flowerbed[index] = 1
            if index != 0 and index != (len(flowerbed)-1):
                if value == 0 and flowerbed[lag] == 0 and flowerbed[lead] == 0:
                    spots_available += 1
                    flowerbed[index] = 1

            lead += 1
            lag += 1

        if n <= spots_available:
            flower_output = True

        return flower_output, flowerbed
