class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        target = 0

        for n in range(len(nums)):
            if nums[n] != 0:
                nums[target], nums[n] = nums[n], nums[target]

                target += 1
