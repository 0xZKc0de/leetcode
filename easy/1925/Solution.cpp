#include <cmath>

class Solution {
public:
    int countTriples(int n) {
        int count = 0;
        
        // Iterate through all possible values for a and b
        for (int a = 1; a <= n; ++a) {
            for (int b = 1; b <= n; ++b) {
                int sumSquares = a * a + b * b;
                
                // Calculate the integer square root
                int c = sqrt(sumSquares);
                
                // Check if c is a perfect square AND if c is within the limit n
                if (c <= n && c * c == sumSquares) {
                    count++;
                }
            }
        }
        
        return count;
    }
};