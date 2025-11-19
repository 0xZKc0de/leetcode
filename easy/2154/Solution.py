class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        lset = set(nums)
        checking = True
        while checking:
            if original in lset:
                original *= 2
            else:
                break

        return original