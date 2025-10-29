class Solution:
    def smallestNumber(self, n: int) -> int:
        s = bin(n)[2:]
        for i in range(0, len(s)):
            if s[i] == 0:
                s[i] = 1
        
        result = 0
        for i in range(0, len(s)):
            result += pow(2, i)
        return result

# Time comlexity : O(k)
# k is the length of element n when we convert it to binary.

