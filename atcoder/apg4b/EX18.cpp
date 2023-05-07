#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    rep(i, M) cin >> A.at(i) >> B.at(i);

    vector<vector<char>> ans(N, vector<char>(N, '-'));

    rep(i, M) {
        ans.at(A.at(i) - 1).at(B.at(i) - 1) = 'o';
        ans.at(B.at(i) - 1).at(A.at(i) - 1) = 'x';
    }

    rep(i, N) {
        rep(j, N) {
            cout << ans.at(i).at(j);
            if (j == N - 1) cout << endl;
            else cout << " ";
        }
    }

}
