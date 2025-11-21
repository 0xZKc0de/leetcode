class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_chars = set(s)
        total_palindromes = 0
        
        for char in unique_chars:
            first = s.find(char)
            last = s.rfind(char)
            if last > first + 1:
                middle_chars = set(s[first+1 : last])
                total_palindromes += len(middle_chars)
                
        return total_palindromes