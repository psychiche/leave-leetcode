# -*- coding: utf-8 -*-
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 遍历
        # 1、如果一直非递减，成功
        # 2、如果有两次下降，失败
        # 3、如果有下降再升，判断升后的值是否比下降前的值小，此时要忽略 nums[0]
        # 4、如果是 nums[0] nums[1] 递减，也成功
        
        n = len(nums)
        if n < 3:
            return True
        
        reverse = 0
        
        for i in range(1, n - 1):
            if nums[i] < nums[i - 1]:
                reverse += 1
                # 2、如果有两次下降，失败
                if reverse == 2:
                    return False
                
                # 4、如果有下降再升，判断升后的值是否比下降前的值小，比较 nums[i+1] nums[i-1];此时要忽略 nums[0]
                # 递减发生在第一位，可忽略
                if i > 1:
                    if nums[i + 1] < nums[i - 1] and nums[i] < nums[i - 2]:
                        return False
        
        # 3、递减发生在最后一位
        if reverse == 1 and nums[-1] < nums[-2]:
            return False
        # 1、如果一直非递减，成功
        return True

