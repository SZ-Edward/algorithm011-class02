# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/longest-common-prefix/
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if not strs:
        return ""
      shortest = sorted(strs, key=len)[0]
      for i, c in enumerate(shortest):
        for other in strs:
          if other[i] != c:
            return shortest[:i]
      return shortest
