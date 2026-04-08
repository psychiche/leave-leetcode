# -*- coding: utf-8 -*-
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 定义 du、du 元素、du 的开始和结束、res 子数组
        n = len(nums)
        if n <= 1:
            return n
        
        # frequency_dict = {num: [f, start, end]}
        frequency_dict = {}
        max_f, most_num, min_len = 0, 0, -1
        
        for i in range(n):
            if nums[i] in frequency_dict:
                frequency_dict[nums[i]][0] += 1
                frequency_dict[nums[i]][2] = i
            else:
                # frequency_dict = {num: [f, start, end]}
                frequency_dict[nums[i]] = [1, i, i]
            # check
            if max_f < frequency_dict[nums[i]][0]:
                max_f = frequency_dict[nums[i]][0]
                most_num = nums[i]
                min_len = frequency_dict[nums[i]][2] - frequency_dict[nums[i]][1] + 1
            elif max_f == frequency_dict[nums[i]][0] and frequency_dict[nums[i]][2] - frequency_dict[nums[i]][
                1] + 1 < min_len:
                most_num = nums[i]
                min_len = frequency_dict[nums[i]][2] - frequency_dict[nums[i]][1] + 1
        
        return min_len


