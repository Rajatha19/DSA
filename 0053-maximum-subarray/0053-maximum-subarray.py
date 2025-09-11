class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algo
        max_sum=curr=nums[0]
        for x in nums[1:]:
            curr=max(x,curr+x)
            max_sum=max(max_sum,curr)
        return max_sum
        
        