#include <algorithm>
#include <cmath>
#include <ctime>
#include <iostream>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

struct Pub {
    int id, x, y;
    float dir;

    Pub(int id, int x, int y) : id(id), x(x), y(y), dir(atan2f(y, x)){};

    bool operator<(const Pub &other) const { return dir < other.dir; }
    bool operator>(const Pub &other) const { return dir > other.dir; }
    bool operator==(const Pub &other) const { return dir == other.dir; }
};

// override cout for Pub.
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
    cout << "is running\n";

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
    sort(pubs.begin(), pubs.end(), [](const Pub &a, const Pub &b) -> bool {
        return pow(a.x, 2) + pow(a.y, 2) < pow(b.x, 2) + pow(b.y, 2);
    });

    // Create ordered set to store good Pubs.
    // Order set by radian angle from origin.
    auto cmp = [](const Pub &a, const Pub &b) -> bool { return a.dir < b.dir; };
    set<Pub, decltype(cmp)> s(cmp);
    // set<Pub> s;

    // Closest element to origin is guaranteed good Pub.
    s.insert(pubs[0]);

    set<Pub>::iterator it, left, right;
    pair<set<Pub>::iterator, bool> ret;

    for (i = 1; i < N; ++i) {
        // If only one good Pub so far, check if current Pub is close.
        if (s.size() == 1 && !near(pubs[i], *s.begin())) {
            s.insert(pubs[i]);
            continue;
        }

        // If two or more good Pubs, find Pub the left and right of current.
        // Try to insert current Pub into set.
        ret = s.insert(pubs[i]);

        // If Pub was not inserted, that means there is a good Pub with
        // same angle closer to origin, which must be inside circle.
        if (!ret.second) continue;

        // If Pub was inserted, check the Pubs immediately to left and right.
        it = left = right = ret.first;

        // If left at beginning loop around to end.
        if (left == s.begin()) left = s.end();

        --left, ++right;

        // If right at end loop around to beginning.
        if (right == s.end()) right = s.begin();

        // If left or right Pub is close, erase added Pub.
        // If neither left or right pub is close, not other Pub can be either.
        if (near(pubs[i], *left) || near(pubs[i], *right)) s.erase(it);
    }

    // Create vector to store good Pubs, then order by id.
    vector<Pub> g(s.begin(), s.end());
    sort(g.begin(), g.end(),
         [](const Pub &a, const Pub &b) -> bool { return a.id < b.id; });

    // Output number of good Pubs, then space separated list of ids in order.
    cout << g.size() << endl;
    for (const Pub& el : g) std::cout << el.id << " ";
    cout << endl << (double)(clock() - tStart) / CLOCKS_PER_SEC << " seconds\n";
    return 0;
}