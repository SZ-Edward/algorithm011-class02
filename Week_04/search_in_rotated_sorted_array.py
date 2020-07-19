# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/search-in-rotated-sorted-array
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
      lo, hi = 0, len(nums) - 1
      while lo < hi:
        mid = (lo + hi) // 2
        if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
          lo = mid + 1
        else:
          hi = mid
      return lo if lo == hi and nums[lo] == target else -1
