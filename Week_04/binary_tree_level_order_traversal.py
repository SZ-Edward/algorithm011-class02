# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
class Solution(object):
    def levelOrder(self, root):
        if not root:
          return []
        res = []

        def dfs(node, depth):
          if depth == len(res):
            res.append([])
          if node:
            res[depth].append(node.val)
          if node.left:
            dfs(node.left, depth + 1)
          if node.right:
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
