# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/combinations/
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      if n <= 0 or k <= 0 or k > n:
        return []
      res = []

      def dfs(start, k, n, res, saved):
        if len(saved) == k:
          res.append(saved[:])
          return
        for i in range(start, n - (k - len(saved)) + 2):
          saved.append(i)
          dfs(i + 1, k, n, res, saved)
          saved.pop()

      dfs(1, k, n, res, [])
      return res
