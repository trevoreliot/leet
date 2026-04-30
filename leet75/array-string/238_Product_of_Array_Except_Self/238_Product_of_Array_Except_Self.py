class Solution:
    # O(N^2)
    def product_except_self(self, nums: list[int]) -> list[int]:

        result_array = []

        for i in range(len(nums)):
            temp_nums = [value for index, value in enumerate(nums) if index != i]
            result = 1
            for num in temp_nums:
                result *= num
            result_array.append(result)

        return result_array


    # O(n)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1] * length

        left_product = 1
        for i in range(length):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(length - 1, -1, -1): # Moving backwards from the end
            result[i] *= right_product
            right_product *= nums[i]

        return result
