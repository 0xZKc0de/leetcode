class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        ls = set(nums)
        tot, max_tot = 1, 1
        new_list = sorted(ls)
        for element in new_list:
            if (element + 1) in ls:
                tot += 1
            else: 
                tot = 1
            if tot >= max_tot :
                max_tot = tot
        return max_tot
        
            
