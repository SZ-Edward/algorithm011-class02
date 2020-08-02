# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/maximum-product-subarray
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      min_res = max_res = res = nums[0]
      for i in range(1, len(nums)):
        if nums[i] < 0:
          min_res, max_res = max_res, min_res
        min_res = min(min_res * nums[i], nums[i])
        max_res = max(max_res * nums[i], nums[i])
        res = max(res, max_res)
      return res
