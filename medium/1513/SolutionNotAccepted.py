class Solution:
    def numSub(self, s: str) -> int:

        # get all the substrings of string.
        def find_substrings(s):
            res = []
            for i in range(len(s)):
                for j in range(i, len(s)):
                    res.append(s[i:j+1])
            return res
        
        count = 0
        arr = find_substrings(s)

        for i in range(1, len(arr) + 1):
            count += arr.count("1" * i)
        return count

        
# This solution did not passed all the tests.
