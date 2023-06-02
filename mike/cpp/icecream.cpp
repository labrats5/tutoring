#include <iostream>
#include <vector>

using namespace std;

int main() {
    int i, n, k, curr, next, count, bottom, mid, top, ans;
    vector<int> stalls;

    cin >> n >> k;
    stalls.reserve(n);
    for (i = 0; i < n; i++) {
        cin >> curr;
        stalls.push_back(curr);
    }

    bottom = ans = 1;
    // stalls 2 <= n
    top = (stalls.back() - stalls.front()) / (k - 1);

    while (bottom <= top) {
        curr = 0;
        count = 1;
        mid = (bottom + top) / 2;

        for (next = 1; next < n; next++) {
            if (stalls[next] - stalls[curr] < mid) continue;

            curr = next;
            count++;
        }

        if (count < k) {
            top = mid - 1;
        } else {
            ans = mid;
            bottom = mid + 1;
        }
    }

    cout << ans << endl;

    return 0;
}