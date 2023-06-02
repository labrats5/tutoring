#include <cmath>
#include <iostream>

using namespace std;

#define EPS 1e-7

int main() {
    double C, bottom, mid, top, ans;
    cin >> C;

    mid = top = sqrt(C);
    bottom = sqrt(C / 2);

    while (bottom < top) {
        mid = (bottom + top) / 2.0;
        ans = pow(mid, 2) + sqrt(mid);
        if (abs(ans - C) < EPS) break;
        (ans < C) ? bottom = mid : top = mid;
    }
    cout << mid << endl;
}