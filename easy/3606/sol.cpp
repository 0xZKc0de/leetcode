#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <cctype>

using namespace std;

class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        unordered_map<string, int> priorityMap = {
            {"electronics", 0},
            {"grocery", 1},
            {"pharmacy", 2},
            {"restaurant", 3}
        };

        vector<pair<int, string>> validCoupons;
        int n = code.size();

        for (int i = 0; i < n; ++i) {
            if (!isActive[i]) continue;
            if (priorityMap.find(businessLine[i]) == priorityMap.end()) continue;

            string s = code[i];
            if (s.empty()) continue;

            bool isCodeValid = true;
            for (char c : s) {
                if (!isalnum(c) && c != '_') {
                    isCodeValid = false;
                    break;
                }
            }

            if (isCodeValid) {
                validCoupons.push_back({priorityMap[businessLine[i]], s});
            }
        }

        sort(validCoupons.begin(), validCoupons.end());

        vector<string> result;
        for (const auto& item : validCoupons) {
            result.push_back(item.second);
        }

        return result;
    }
};