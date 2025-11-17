class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k 
        
        for element in nums:
            if element != 1:
                count += 1
            else:
                if count < k:
                    return False
                count = 0
                
        return True
    
