#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); ++i)

int main() {
    int N;
    cin >> N;

    vector<tuple<int, int>> L(N);
    int a, b;
    rep(i, N) {
        cin >> a >> b;
        L.at(i) = make_tuple(b, a);
    }
    sort(L.begin(), L.end());
    rep(i, N) {
        tie(b, a) = L.at(i);
        cout << a << " " << b << endl;
    }
}
