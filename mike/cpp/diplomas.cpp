#include <cmath>
#include <iostream>

using namespace std;

int main() {
    long w, h, n, bottom, top, middle, ans;
    cin >> w >> h >> n;

    bottom = ceil(sqrt(n)) * min(w, h);
    ans = top = ceil(sqrt(n)) * max(w, h);

    while (bottom <= top) {
        middle = (bottom + top) / 2;
        if ((middle / w) * (middle / h) < n) {
            bottom = middle + 1;
        } else {
            ans = middle;
            top = middle - 1;
        }
    }
    cout << ans;
}