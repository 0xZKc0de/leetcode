class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        remainder = total_sum % 3
        
        if remainder == 0:
            return total_sum
   
        ones = sorted([x for x in nums if x % 3 == 1])
        twos = sorted([x for x in nums if x % 3 == 2])
        

        if remainder == 1:


            ans1 = total_sum - ones[0] if ones else 0

            ans2 = total_sum - sum(twos[:2]) if len(twos) >= 2 else 0
            return max(ans1, ans2)
 
        elif remainder == 2:
            ans1 = total_sum - twos[0] if twos else 0
            ans2 = total_sum - sum(ones[:2]) if len(ones) >= 2 else 0
            return max(ans1, ans2)
            
        return 0


# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(n) for storing the ones and twos lists