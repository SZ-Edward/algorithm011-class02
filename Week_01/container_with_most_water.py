# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/container-with-most-water/
"""
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    result = 0
    while left < right:
        result = max(result, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result
