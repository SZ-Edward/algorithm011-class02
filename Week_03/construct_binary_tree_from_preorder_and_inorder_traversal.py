# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
          return None
        root = TreeNode(preorder[0])
        curr_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:curr_index + 1], inorder[:curr_index])
        root.right = self.buildTree(preorder[curr_index + 1:], inorder[curr_index + 1:])
        return root
