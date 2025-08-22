class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        a=nums[0:n-k]
        b=nums[n-k:n]
        nums[:]=b+a