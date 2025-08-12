class Solution:
    def isPalindrome(self, x: int) -> bool:
        normal=str(x)
        rev=normal[::-1]
        return normal==rev