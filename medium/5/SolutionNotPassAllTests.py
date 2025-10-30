class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s

        lst = []
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                if self.isPalindrom(s[i:j]):
                    lst.append(s[i:j])
        
        lst.sort(key=len)
        return lst[-1]

    def isPalindrom(self, s: str) -> bool:
        i, j = 0, len(s) -1
        while(i <= j):
            if s[i] == s[j]:
                i +=1
                j -=1
            else:
                return False
        return True

# Time Complexity: O(N³)
# Space Complexity: O(N²)
