# -*- coding: utf-8 -*-
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 每轮选择一个最大的
        # 排序，相加再排序
        n = len(nums)
        cnt = 0
        if n == 1:
            return cnt
        nums.sort()
        
        while
