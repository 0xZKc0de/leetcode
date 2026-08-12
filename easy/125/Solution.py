class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left].lower() not in alphabet:
                left += 1
                continue
            if s[right].lower() not in alphabet:
                right -= 1
                continue
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True

        
