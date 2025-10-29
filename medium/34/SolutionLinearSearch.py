class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target not in nums:
            return [-1, -1]


        i, j = 0, len(nums) -1
        while i <= j:
            if nums[i] != target and nums[j] != target:
                i +=1
                j -=1
            elif nums[i] != target and nums[j] == target:
                i +=1
            
            elif nums[i] == target and nums[j] != target:
                j -=1
            else :
                return [i, j]
            


# Time Complexity : O(N)
# this is code is using just the Linear Search, not the Binary Search, but he is accepted in Leetcode.
