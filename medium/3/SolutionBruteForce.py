class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        result = 0
        for i in range(0, len(s)):
            tmp = 0
            rlist = []
            for j in range(i, len(s)):
                if s[j] not in rlist:
                    tmp += 1
                    rlist.append(s[j])
                else:
                    rlist = []
                    if tmp > result:
                        result = tmp
                    break
        
            if tmp > result:
                result = tmp
        return result

# Time complexity: O(N²)
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

