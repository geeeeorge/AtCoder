#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main() {
    int N;
    cin >> N;
    vector<int> A(N);

    rep(i, N) {
        cin >> A.at(i);
    }

    int mean = accumulate(A.begin(), A.end(), 0) / N;

    rep(i, N) cout << abs(A.at(i) - mean) << endl;
}
