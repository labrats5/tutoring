#include <cmath>
#include <iostream>

using namespace std;

int main() {
    double M, R, y;
    int N, P, x;
    cin >> M >> R;
    R /= M;
    N = (int)ceil(R);
    P = 0;

    // x = R * cos(θ), θ = 45°
    // x = ceil(R * sqrt(2) / 2)
    for (x = 1; x < N; x++) {
        y = sqrt(R*R - x*x);
        if (y == round(y)) P++;
    }

    cout << (N + N - 1 - P) * 4 << endl;
    return 0;
}