# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/permutations-ii/
"""
class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
          ans = [l[:i]+[n]+l[i:]
                 for l in ans
                 for i in xrange((l+[n]).index(n) + 1)]
        return ans
