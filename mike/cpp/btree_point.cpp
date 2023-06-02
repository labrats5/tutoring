#include <cmath>
#include <iostream>
#include <string>

#include "binary_tree.h"

using namespace std;

struct Point {
    int x, y;

    Point(int x, int y) : x(x), y(y) {}

    Point add(Point a, Point b);
    double dist() const { return sqrt(x * x + y * y); }
    double angle() const { return atan2(y, x); }

    bool operator<(const Point &other) const { return dist() < other.dist(); }
    bool operator>(const Point &other) const { return dist() > other.dist(); }
    bool operator==(const Point &other) const {
        return x == other.x && y == other.y;
    }
};

Point Point::add(Point a, Point b) { return Point(a.x + b.x, a.y + b.y); }

ostream &operator<<(ostream &out, const Point &p) {
    out << "x: " << p.x << "\ty: " << p.y << "\tdist: " << p.dist();
    return out;
}

int main() {
    Tree<Point> tree = Tree<Point>();
    tree.insert(Point(34, 55));
    tree.insert(Point(18, 91));
    tree.insert(Point(56, 97));
    tree.insert(Point(16, 17));
    tree.insert(Point(26, 37));
    tree.insert(Point(16, 107));

    // tree.erase(Point(34, 55));
    // tree.erase(Point(56, 97));
    // tree.erase(Point(12, 18));
    // tree.erase(Point(16, 107));
    cout << tree.size << endl;
    tree.inorder();
    vector<Point> vp = tree.to_vector();
    for (Point el : vp) cout << el << endl;
}