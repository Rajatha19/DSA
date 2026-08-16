class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import re

        words = re.findall(r'\w+', paragraph.lower())
        count = dict(Counter(words))

        ans = ""
        max_count = 0

        for key, value in count.items():
            if key not in banned and value > max_count:
                ans = key
                max_count = value

        return ans
        