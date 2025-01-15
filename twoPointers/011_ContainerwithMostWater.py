"""
Two Pointers 
왼쪽의 높이가 작다면 왼쪽 index += 1 오른쪽의 높이가 작다면 오른쪽 index -= 1
두 포인터들을 가운데로 iterate하면서 면적계산. O(n)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water, n = 0, len(n)
        left, right = 0, n - 1
        while left < right:
            if height[left] > height[right]:
                max_water = max(height[right] * (right - left), max_water)
                right -= 1
            elif height[left] <= height[right]:
                max_water = max(height[left] * (right - left), max_water)
                left += 1
        return max_water