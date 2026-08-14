from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                d = Counter(substring)

                isTrue = True
                for key, value in d.items():
                    if value > 2:
                        isTrue = False 
                        break

                if isTrue:
                    if len(substring) > max_length:
                        max_length = len(substring)
                        
        return max_length
