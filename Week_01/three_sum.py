# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/3sum/
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res, length = [], len(nums)
    nums.sort()
    for i in range(length - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, length - 1
        while left < right:
            ssum = nums[i] + nums[left] + nums[right]
            if ssum < 0:
                left += 1
            elif ssum > 0:
                right -= 1
            else:
                res.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res
