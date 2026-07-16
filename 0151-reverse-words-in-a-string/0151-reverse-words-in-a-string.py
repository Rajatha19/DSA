class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.strip().split()
        b=(a[::-1])
        c=" ".join(b)
        return c