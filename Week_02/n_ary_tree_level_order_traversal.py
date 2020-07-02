# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
"""
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
      if not root:
        return []

      result = []
      queue = collections.deque([root])
      while queue:
        level = []
        for _ in range(len(queue)):
          node = queue.popleft()
          level.append(node.val)
          queue.extend(node.children)
        result.append(level)
      return result
