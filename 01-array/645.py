# -*- coding: utf-8 -*-
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        num_set = set([i for i in range(1, n + 1)])
        res = [0, 0]
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                res[0] = num
        res[1] = num_set.pop()
        
        return res
