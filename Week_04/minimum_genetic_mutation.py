# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/minimum-genetic-mutation/
"""
class Solution(object):
    def minMutation(self, start, end, bank):
        bank, visited, queue = set(bank), {start}, [(start, 0)]
        for seq, k in queue:
          for s in (seq[:i] + cc + seq[i + 1:] for i, c in enumerate(seq) for cc in 'ACGT'):
            if s not in visited and s in bank:
              if s == end:
                return k + 1
              queue.append((s, k + 1))
              visited.add(s)
        return -1
