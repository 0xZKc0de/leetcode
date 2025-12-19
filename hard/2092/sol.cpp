class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        sort(meetings.begin(), meetings.end(), [](const auto& a, const auto& b) {
            return a[2] < b[2];
        });

        vector<int> p(n);
        iota(p.begin(), p.end(), 0);
        p[firstPerson] = 0;

        function<int(int)> find = [&](int x) {
            return p[x] == x ? x : (p[x] = find(p[x]));
        };

        int m = meetings.size();
        for (int i = 0; i < m; ) {
            int j = i;
            while (j < m && meetings[j][2] == meetings[i][2]) j++;

            for (int k = i; k < j; ++k) {
                int u = find(meetings[k][0]);
                int v = find(meetings[k][1]);
                if (u != v) {
                    if (u == 0) p[v] = 0;
                    else if (v == 0) p[u] = 0;
                    else p[u] = v;
                }
            }

            for (int k = i; k < j; ++k) {
                if (find(meetings[k][0]) != 0) {
                    p[meetings[k][0]] = meetings[k][0];
                    p[meetings[k][1]] = meetings[k][1];
                }
            }
            i = j;
        }

        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (find(i) == 0) res.push_back(i);
        }
        return res;
    }
};