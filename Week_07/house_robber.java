# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/house-robber/
"""
class Solution {
    public int rob(int[] nums) {
      if (nums == null || nums.length == 0) return 0;
      int n = nums.length;
      int[][] dp = new int[n][2];
      dp[0][0] = nums[0];
      dp[0][1] = 0;
      for(int i = 1; i < n; ++ i) {
        dp[i][0] = dp[i-1][1] + nums[i];
        dp[i][1] = Math.max(dp[i-1][0], dp[i-1][1]);
      }
      return Math.max(dp[n-1][0], dp[n-1][1]);
    }
}
