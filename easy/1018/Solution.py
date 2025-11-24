class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        result = 0
        
        for bit in nums:
            result = (result * 2 + bit) % 5

            answer.append(result == 0)
            
        return answer