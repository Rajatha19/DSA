class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc=result=0
        for num in nums:
            if num==1:
                result+=1
                maxc=max(maxc,result)
            else:
                result=0
        return maxc