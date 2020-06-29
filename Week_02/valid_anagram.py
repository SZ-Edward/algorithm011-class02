# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/valid-anagram/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      return len(s) == len(t) and sorted(s) == sorted(t)
