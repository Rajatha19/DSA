class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        maxi=nums[0]
        for num in nums:
            curr=max(num+curr,num)
            maxi=max(curr,maxi)
        return maxi


        