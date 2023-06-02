#include <iostream>

using namespace std;

struct Position2D {
    double x, y;

    // Position2D(double x, double y) : x(x), y(y) {}
};

struct Position3D: Position2D {
    double z;

    // Position3D(double x, double y, double z) : Position2D(x, y), z(z) {}
};

int main() {
    Position3D p{2.0, 3.0, 4.0};
    cout << p.x << endl << p.y << endl << p.z << endl;

    return 0;
}