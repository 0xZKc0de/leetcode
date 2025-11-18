class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        arr = []
        while len(bits) != 0:
            if bits[0] == 0:
                arr.append(bits.pop(0))
            else:
                arr.append(bits.pop(0) + bits.pop(0))
        return True if arr[-1] == 0 else False