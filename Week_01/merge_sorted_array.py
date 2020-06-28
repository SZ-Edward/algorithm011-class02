# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/merge-sorted-array/
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0
        nums1_copy = nums1[:m]
        while i < len(nums1_copy) and j < len(nums2):
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while i < len(nums1_copy):
            nums1[k] = nums1_copy[i]
            i, k = i + 1, k + 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            j, k = j + 1, k + 1
