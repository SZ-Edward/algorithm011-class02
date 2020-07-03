# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
      def dfs(left, right):
          if left > right:
            return 

          mid = (left + right) // 2
          root = TreeNode(nums[mid])
          root.left = dfs(left, mid - 1)
          root.right = dfs(mid + 1, right)
          return root

      return dfs(0, len(nums) - 1)
