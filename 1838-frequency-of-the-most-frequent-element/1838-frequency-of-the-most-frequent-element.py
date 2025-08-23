class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        result=0
        su=0
        for right in range (len(nums)):
            su+=nums[right]
            while nums[right]*(right-left+1)>k+su:
                su-=nums[left]
                left+=1
            result=max(result,right-left+1)
        return result 

        