#include <algorithm>
#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

#include "binary_tree.h"

using namespace std;

struct Pub {
    int id, x, y;
    float dir;

    Pub(int id, int x, int y) : id(id), x(x), y(y), dir(atan2f(y, x)){};

    bool operator<(const Pub &other) const { return dir < other.dir; }
    bool operator>(const Pub &other) const { return dir > other.dir; }
    bool operator==(const Pub &other) const { return dir == other.dir; }
};

// override cout << for Pub.
ostream &operator<<(ostream &out, const Pub &p) {
    out << "id: " << p.id << "\tx: " << p.x << "\ty: " << p.y
        << "\tdir: " << p.dir;
    return out;
}

// Calculate if Pub b is within the circle defined by origin and Pub a.
bool near(const Pub &a, const Pub &b) {
    double cx, cy, rsq;
    cx = a.x / 2.0;
    cy = a.y / 2.0;
    rsq = pow(cx, 2) + pow(cy, 2);
    return pow(b.x - cx, 2) + pow(b.y - cy, 2) <= rsq;
}

int main(int argc, const char *argv[]) {
    clock_t tStart = clock();
    std::cout << "is running\n";

    int i, x, y, N, R;

    if (argc < 2) {
        cin >> N;
    } else {
        N = stoi(std::string(argv[1]));
    }

    R = (N / 100) * (N / 100);

    // Vector to store all Pubs.
    vector<Pub> pubs;
    pubs.reserve(N);
    for (i = 0; i < N; ++i) {
        x = round(R * cos(2 * M_PI * i / N));
        y = round(R * sin(2 * M_PI * i / N));
        pubs.push_back(Pub(i + 1, x, y));
    }

    // Order Pubs by distance from origin.
    std::sort(pubs.begin(), pubs.end(), [](const Pub &a, const Pub &b) -> bool {
        return pow(a.x, 2) + pow(a.y, 2) < pow(b.x, 2) + pow(b.y, 2);
    });

    // Closest element to origin is guaranteed good Pub.
    Tree<Pub> t = Tree<Pub>();
    Node<Pub> *left, *right;
    t.insert(pubs[0]);

    for (i = 1; i < N; ++i) {
        // If only one good Pub so far, check if current Pub is close.
        if (t.size == 1 && !near(pubs[i], t.root->value)) {
            t.insert(pubs[i]);
            continue;
        }

        // If search is not NULL, then there is a good Pub with
        // same angle closer to origin, which must be inside circle.
        if (t.search(pubs[i])) continue;

        // Check the Pubs immediately to left and right.
        left = t.lower_bound(pubs[i]);
        right = t.upper_bound(pubs[i]);

        // If left is NULL loop around to end.
        // If right is NULL loop around to beginning.
        if (!left) left = t.back();
        if (!right) right = t.front();

        // If neither left or right pub is close, not other Pub can be either.
        if (!near(pubs[i], left->value) && !near(pubs[i], right->value)) {
            t.insert(pubs[i]);
        }
    }

    // Create vector to store good Pubs, then order by id.
    vector<Pub> g;
    t.to_vector(g);

    std::sort(g.begin(), g.end(),
              [](const Pub &a, const Pub &b) -> bool { return a.id < b.id; });

    // Output number of good Pubs, then space separated list of ids in order.
    std::cout << g.size() << endl;
    for (const Pub &el : g) std::cout << el.id << " ";
    std::cout << endl
              << (double)(clock() - tStart) / CLOCKS_PER_SEC << " seconds\n";
    return 0;
}