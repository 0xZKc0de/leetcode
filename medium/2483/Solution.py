class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current_score = 0
        max_score = 0
        best_hour = 0

        for i, char in enumerate(customers):
            if char == 'Y':
                current_score += 1
            else:
                current_score -= 1
            
            if current_score > max_score:
                max_score = current_score
                best_hour = i + 1
                
        return best_hour