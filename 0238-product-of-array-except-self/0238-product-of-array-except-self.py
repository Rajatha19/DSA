class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        pre=1
        post=1
        answer=[1]*length
        for i in range(length):
            answer[i]*=pre
            pre=pre*nums[i]
            answer[length-i-1]*=post
            post=post*nums[length-i-1]
        return answer
