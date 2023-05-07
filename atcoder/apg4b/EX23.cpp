#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    rep(i, N) cin >> A.at(i);

    map <int, int> mp;
    rep(i, N) mp[A.at(i)]++;

    int max_cnt = 0;
    int max_num = 0;
    for (auto p : mp) {
        if (max_cnt < p.second) {
            max_cnt = p.second;
            max_num = p.first;
        }
    }
    cout << max_num << " " << max_cnt << endl;

}
