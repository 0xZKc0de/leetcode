class Solution:
    def maxScore(self, s: str) -> int:

        zeros_left = 1 if s[0] == '0' else 0
        
        ones_right = 0
        for i in range(1, len(s)):
            if s[i] == '1':
                ones_right += 1

        max_score = zeros_left + ones_right
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else: 
                ones_right -= 1
            current_score = zeros_left + ones_right

            if current_score > max_score:
                max_score = current_score
                
        return max_score


