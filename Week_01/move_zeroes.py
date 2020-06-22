# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/move-zeroes/
"""
def moveZeroes(nums):
    i = 0        
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
