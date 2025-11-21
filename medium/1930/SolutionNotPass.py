from typing import List
from itertools import combinations

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:


        def get_all_subsequences(s: str) -> List[str]:
            combs = combinations(s, 3)
            result = set("".join(item) for item in combs)
            return list(result)
        
        def isPalindrom(s: str) -> bool:
            if s[0] == s[-1]:
                return True
            return False
        count = 0
        result = get_all_subsequences(s)
        for element in result:
            if isPalindrom(element):
                count += 1
        return count