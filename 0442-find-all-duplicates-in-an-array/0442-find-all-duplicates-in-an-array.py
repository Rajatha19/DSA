class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count=Counter(nums)
        res=[]
        for key,value in count.items():
            if value==2:
                res.append(key)
        return res