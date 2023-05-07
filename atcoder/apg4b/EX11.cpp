#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main() {
    int N, A;
    cin >> N >> A;

    rep(i, N) {
        string op;
        int B;
        cin >> op >> B;

        if (op == "+") {
            A += B;
        } else if (op == "-") {
            A -= B;
        } else if (op == "*") {
            A *= B;
        } else if (op == "/" && B != 0) {
            A /= B;
        } else {
            cout << "error" << endl;
            break;
        }

        cout << i + 1 << ":" << A << endl;
    }

}
