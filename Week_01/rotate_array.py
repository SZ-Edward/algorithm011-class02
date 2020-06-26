# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/rotate-array/
"""
def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
