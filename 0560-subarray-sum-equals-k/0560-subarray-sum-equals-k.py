class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result=0
        curr=0
        cm={0:1}
        for num in nums:
            curr+=num
            if curr-k in cm:
                result+=cm[curr-k]
            if curr in cm:
                cm[curr]+=1
            else:
                cm[curr]=1
        return result
                