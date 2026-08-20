class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [], [] 
        arr1.append(nums[0])
        del nums[0]
        arr2.append(nums[0])
        del nums[0]
        while(len(nums) != 0):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[0])
                del nums[0]
            else:
                arr2.append(nums[0])
                del nums[0]     
        
        return arr1 + arr2

