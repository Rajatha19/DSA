class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        result=[]
        for num in freq:
            result.extend([num] * min(freq[num],2))
        nums[:]=result
