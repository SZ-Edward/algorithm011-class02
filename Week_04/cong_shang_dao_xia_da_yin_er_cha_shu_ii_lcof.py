# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      if not root:
        return []
      res, queue = [], [root]
      while queue:
        node = queue.pop()
        if not node:
          return
        level = [node.val]
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
        res.append(level)
      return res
