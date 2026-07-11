class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums.copy()

        for i in range(2, len(nums)):
            dp[i] += max(dp[:i-1])
        
        return max(dp)