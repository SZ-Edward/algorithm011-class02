# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""
def largest_rectangle_area(heights):
    _heights = [-1] + heights + [-1]  
    length = len(_heights)
    max_area = 0
    stack = [0]  

    for i in range(1, length):
        while _heights[i] < _heights[stack[-1]]:
            height = _heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)  
    return max_area
