class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)
        
        total_sum = sum(nums)
        max_sum = float('-inf')
        for i in range(1, len(prefix_sum)):
            for j in range(i):
                sub_sum = prefix_sum[i] - prefix_sum[j]
                max_sum = max(max_sum, sub_sum)
                if i - j < len(nums):
                    max_sum = max(max_sum, total_sum - sub_sum)
        
        return max_sum