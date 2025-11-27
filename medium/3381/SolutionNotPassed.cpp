class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        
        vector<long long> prefix(n + 1, 0);

        for(int i = 0; i < n; i++){
            prefix[i+1] = prefix[i] + nums[i];
        }

        long long max_sum = -1e18; 
        
        vector<int> kk;
        int m = 1;
        while(true){
            if(k * m <= n){
                kk.push_back(k * m);
                m++;
            }
            else{
                break;
            }

        }

        for(int j = 0; j < kk.size(); j++){
            k = kk[j];
            for(int i = k; i <= n; i++){
                long long current_sum = prefix[i] - prefix[i-k];
                max_sum = max(max_sum, current_sum);
            }
        }
        return max_sum;
    }
};