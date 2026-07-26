class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need=Counter(t)
        window=defaultdict(int)
        req=len(need)
        formed=0
        min_len=float('inf')
        l=0
        start=0
        for r in range(len(s)):
            char=s[r]
            window[char]+=1
            if char in need and window[char]==need[char]:
                formed+=1
            while formed==req:
                if r-l+1<min_len:
                    min_len=r-l+1
                    start=l
                l_char=s[l]
                window[l_char]-=1
                if l_char in need and window[l_char]<need[l_char]:
                    formed-=1
                l+=1
        if min_len==float('inf'):
            return ""
        return s[start:start+min_len]