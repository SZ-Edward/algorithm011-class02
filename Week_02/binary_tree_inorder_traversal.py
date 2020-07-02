# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/binary-tree-inorder-traversal
"""
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        WHITE, GRAY = 1, 0
        stack = [(WHITE, root)]
        while stack:
          color, node = stack.pop()
          if not node: 
            continue
          if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((GRAY, node))
            stack.append((WHITE, node.left))
          else:
            res.append(node.val)
        return res
