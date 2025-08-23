class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            sorted_arr=nums[i:]+nums[:i]
            if sorted_arr==sorted(nums):
                return True
        return False
        
        
        '''
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
            if count>1:
                return False
        return True     '''   