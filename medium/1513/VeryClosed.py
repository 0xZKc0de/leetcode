class Solution:
    def numSub(self, s: str) -> int:

        # get all the substrings of string.
        def find_substrings(s):
            res = []
            for i in range(len(s)):
                for j in range(i, len(s)):
                    if len(set(s[i:j+1])) == 1 and list(set(s[i:j+1]))[0] == "1":
                        res.append(s[i:j+1])
            return len(res)
        
        return find_substrings(s)
        

# Very closed, but still did not passed all the tests, i think he is need complexity less then O(N*N).