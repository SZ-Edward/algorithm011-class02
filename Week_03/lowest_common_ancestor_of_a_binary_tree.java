# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left == null) return right;
        if (right == null) return left;
        if (left != null && right != null) return root;
        return null;
    }
}
