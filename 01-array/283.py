# -*- coding: utf-8 -*-
from collections import deque


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        
        z_idx, nz_idx = deque(), 0
        
        while nz_idx < n:
            # 获取第一个 0
            if nums[nz_idx] == 0:
                z_idx.append(nz_idx)
                nz_idx += 1
            else:
                # 如果之前没有0 值，不交换；如果之前有 0 值，执行交换
                if not z_idx:
                    nz_idx += 1
                else:
                    zero_idx = z_idx.popleft()
                    nums[zero_idx], nums[nz_idx] = nums[nz_idx], nums[zero_idx]





class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

