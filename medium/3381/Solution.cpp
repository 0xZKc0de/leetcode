class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();

        vector<long long> min_prefix(k, 1e18); 

        min_prefix[0] = 0; 

        long long current_sum = 0;
        long long max_sum = -1e18; 

        for (int i = 1; i <= n; ++i) {
            current_sum += nums[i-1];

            int rem = i % k;

            if (min_prefix[rem] != 1e18) {
                max_sum = max(max_sum, current_sum - min_prefix[rem]);
            }

            min_prefix[rem] = min(min_prefix[rem], current_sum);
        }

        return max_sum;
    }
};