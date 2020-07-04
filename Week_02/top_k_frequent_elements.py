# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      d = {}
      for each in nums:
        d[each] = d.get(each, 0) + 1
      tps = sorted(d.items(), key=lambda item: item[1], reverse=True)[:k]
      return [tp[0] for tp in tps]
