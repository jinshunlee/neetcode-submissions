class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        for i, i_height in enumerate(heights):
            for j in range(i + 1, len(heights)):
                largestArea = max(min(i_height, heights[j]) * (j - i), largestArea)
        return largestArea

        