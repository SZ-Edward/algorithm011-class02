# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
          return []
        stack, output = [root,], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(node.children[::-1])

        return output
