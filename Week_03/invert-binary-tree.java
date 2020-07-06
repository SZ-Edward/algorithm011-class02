# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/invert-binary-tree
"""
class Solution {
    public TreeNode invertTree(TreeNode root) {
      if (root == null) return null;
      TreeNode tmp = root.left;
      root.left = root.right;
      root.right = tmp;
      invertTree(root.left);
      invertTree(root.right);
      return root;
    }
}
