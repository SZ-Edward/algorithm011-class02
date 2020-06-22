# !/usr/bin/env python
# encoding: utf-8

"""
  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""
def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return 1

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
