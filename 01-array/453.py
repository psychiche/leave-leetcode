class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        if n == 1:
            return cnt
        nums.sort()
        
        for i in range(1, n):
            cnt += nums[i] - nums[0]
        
        return cnt
