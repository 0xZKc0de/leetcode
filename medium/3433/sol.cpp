#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

class Solution {
public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        sort(events.begin(), events.end(), [](const vector<string>& a, const vector<string>& b) {
            int t1 = stoi(a[1]);
            int t2 = stoi(b[1]);
            if (t1 != t2) {
                return t1 < t2;
            }
            return a[0] == "OFFLINE";
        });

        vector<int> mentions(numberOfUsers, 0);
        vector<int> onlineUntil(numberOfUsers, 0);

        for (const auto& event : events) {
            string type = event[0];
            int time = stoi(event[1]);
            string content = event[2];

            if (type == "OFFLINE") {
                int id = stoi(content);
                onlineUntil[id] = time + 60;
            } else {
                if (content == "ALL") {
                    for (int i = 0; i < numberOfUsers; ++i) {
                        mentions[i]++;
                    }
                } else if (content == "HERE") {
                    for (int i = 0; i < numberOfUsers; ++i) {
                        if (onlineUntil[i] <= time) {
                            mentions[i]++;
                        }
                    }
                } else {
                    stringstream ss(content);
                    string token;
                    while (ss >> token) {
                        int id = stoi(token.substr(2));
                        mentions[id]++;
                    }
                }
            }
        }
        return mentions;
    }
};