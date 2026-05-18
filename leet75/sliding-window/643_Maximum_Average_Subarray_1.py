class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
# Calculate the sum of the very first window
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Add the new element coming in, subtract the old element going out
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k
