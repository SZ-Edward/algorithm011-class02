# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
"""
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
      if not root:
        return []

      res, queue = [], [(root, 0)]
      while queue:
        node, level = queue.pop(0)
        if level == len(res):
          res.append(node.val)
        res[level] = max(res[level], node.val)
        if node.left:
          queue.append((node.left, level + 1))
        if node.right:
          queue.append((node.right, level + 1))

      return res
