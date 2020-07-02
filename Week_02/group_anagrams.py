# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/group-anagrams/
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      d = collections.defaultdict(list)
      for item in sorted(strs):
        d[tuple(sorted(item))].append(item)
      return d.values()
