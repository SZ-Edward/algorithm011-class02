# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        WHITE, GRAY = 1, 0
        stack = [(WHITE, root)]
        while stack:
          color, node = stack.pop()
          if not node: 
            continue
          if color == WHITE:         
            stack.append((WHITE, node.right)) 
            stack.append((WHITE, node.left))  
            stack.append((GRAY, node))            
          else:
            result.append(node.val)
        return result
