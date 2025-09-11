class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_sum=float('-inf')
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>max_sum:
                max_sum=sum
            if sum<0:
                sum=0
        return max_sum


       
       
       
    '''
        #kadane's algo
        max_sum=curr=nums[0]
        for x in nums[1:]:
            curr=max(x,curr+x)
            max_sum=max(max_sum,curr)
        return max_sum
        '''
        