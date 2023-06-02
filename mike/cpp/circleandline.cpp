#include <iostream>
#include <cmath>

using namespace std;

const double EPS = 1e-8;

int main() {
    double r0, x0, y0, x1, y1, x2, y2, y;
    cin >> r0 >> x0 >> y0 >> x1 >> y1 >> x2 >> y2;

    if (x1 == x2) {
        y = r0*r0 - pow(x1-x0, 2);
        if (y < -EPS) {
            cout << -1 << endl;
            return 0;
        }
        if (abs(y) < EPS) {
            cout << 0 << endl;
            return 0;
        }

        cout << 2 * y << endl;
        return 0;
    }

    double k, b0, a, b, c, det, p1x, p2x, p1y, p2y, dist;
    k = (y2 - y1) / (x2 - x1);
    b0 = y1 - (k * x1);

    a = k*k + 1;
    b = 2*b0*k - 2*y0*k - 2*x0;
    c = x0*x0 + b0*b0 - 2*b0*y0 + y0*y0 - r0*r0;

    det = (b*b) - (4*a*c);
    if (det < -EPS) {
        cout << -1 << endl;
        return 0;
    }
    if (abs(det) < EPS) {
        cout << 0 << endl;
        return 0;
    }
    p1x = (-b + sqrt(det)) / (2 * a);
    p2x = (-b - sqrt(det)) / (2 * a);
    p1y = k*p1x + b0;
    p2y = k*p2x + b0;

    dist = sqrt(pow(p2x - p1x, 2) + pow(p2y - p1y, 2));
    if (dist < 0.000001) {
        cout << 0 << endl;
        return 0;
    }
    cout << dist << endl;

    return 0;
}