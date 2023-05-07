#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, S;
    cin >> N >> S;
    vector<int> A(N), P(N);
    rep(i, N) cin >> A.at(i);
    rep(i, N) cin >> P.at(i);

    // リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
    // ここにプログラムを追記
    int ans = 0;
    rep(i, N) rep(j, N) if (A.at(i) + P.at(j) == S) ans++;
    cout << ans << endl;
}
