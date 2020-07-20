# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/search-insert-position
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      length = len(nums)
      if length == 0:
        return 0
      left, right = 0, length
      while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
          return mid
        elif nums[mid] > target:
          right = mid
        else:
          left = mid + 1
      return left
