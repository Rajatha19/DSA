class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x*=sign
        rev=0
        while x>0:
            last=x%10
            x=x//10
            if rev>(2**31-1)//10:
                return 0
            rev=rev*10+last
        return rev*sign