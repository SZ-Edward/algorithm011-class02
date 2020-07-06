# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/validate-binary-search-tree/
"""
class Solution {
    long pre = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        if (!isValidBST(root.left)) return false;
        if (root.val <= pre) return false;
        pre = root.val;
        return isValidBST(root.right);
    }
}
