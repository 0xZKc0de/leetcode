#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        long long originalProfit = 0;
        int n = prices.size();
        
        for (int i = 0; i < n; ++i) {
            originalProfit += (long long)strategy[i] * prices[i];
        }
        
        long long currentWindowSum = 0;
        long long newWindowSum = 0;
        int halfK = k / 2;
        
        for (int i = 0; i < k; ++i) {
            currentWindowSum += (long long)strategy[i] * prices[i];
            if (i >= halfK) {
                newWindowSum += prices[i];
            }
        }
        
        long long maxDiff = max(0LL, newWindowSum - currentWindowSum);
        
        for (int i = k; i < n; ++i) {
            currentWindowSum += (long long)strategy[i] * prices[i];
            currentWindowSum -= (long long)strategy[i - k] * prices[i - k];
            
            newWindowSum += prices[i];
            newWindowSum -= prices[i - halfK];
            
            maxDiff = max(maxDiff, newWindowSum - currentWindowSum);
        }
        
        return originalProfit + maxDiff;
    }
};