# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
      if not root:
        return []
      stack, output = [root, ], []
      while stack:
        node = stack.pop()
        if node:
          for each in node.children:
            stack.append(each)
          output.append(node.val)
      return output[::-1]
