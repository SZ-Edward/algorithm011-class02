# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/two-sum/
"""
def twoSum(nums, target):
    data = {}
    for i in range(len(nums)):
        another = target - nums[i]
        if another in data:
            return [data[another], i]
        data.update({nums[i]: i})
