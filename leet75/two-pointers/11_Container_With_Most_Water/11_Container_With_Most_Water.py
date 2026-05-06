class Solution:
    def maxArea(self, height: list[int]) -> int:
        #Plan:  We need to multiply the min of our y axis and our x axis pointer
        # and select greatest area combo

        max_area = 0

        right = len(height)-1
        left = 0

        while right > left:

            y = min(height[left], height[right])
            x = right - left

            area = y * x
            if area > max_area:
                max_area = area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
