class Solution:

    def increasingTriplet(self, nums: list[int]) -> bool:

        """We need to progress through the list nums and find a triplet ONCE"""
        """(who cares how many there are)."""
        """Lets store numbers based on their values relative the minimum scanned so far."""

        i = float("inf") # Placeholder for i
        j = float("inf") # Placeholder for j

        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True # We found k

        return False


    def increasingTripletSubarray(self, nums: list[int]) -> bool:

        output = False

        for x in range(1, len(nums)-1):

            i = nums[x-1]
            j = nums[x]
            k = nums[x+1]

            if i < j < k:
                output = True

        return output
