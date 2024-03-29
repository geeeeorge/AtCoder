#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    vector<int> data(5);
    for (int i = 0; i < 5; i++) {
        cin >> data.at(i);
    }

    // dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
    bool ans = false;
    rep(i, 4) {
        if (data.at(i) == data.at(i + 1)) {
            ans = true;
            break;
        }
    }
    cout << (ans ? "YES" : "NO") << endl;
}
