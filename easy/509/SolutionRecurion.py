class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else :
            return self.fib(n-1) + self.fib(n-2)
        

# Using the recursion, the time complexity of this solution is O(2^n)
# and the space complexity is O(n) due to the maximum depth of the recursion stack.