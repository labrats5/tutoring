#include <algorithm>
#include <cmath>
#include <ctime>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

struct Pub {
    int id, x, y;

    // Pub(int id, int x, int y) : id(id), x(x), y(y) {};
};

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
    // Create list of Pubs roughly in shape of a circle around the origin.
    for (i = 0; i < N; ++i) {
        x = round(R * cos(2 * i * M_PI / N));
        y = round(R * sin(2 * i * M_PI / N));
        pubs.push_back(Pub{i + 1, x, y});
    }

    // Order Pubs by distance from origin.
    sort(pubs.begin(), pubs.end(), [](const Pub &a, const Pub &b) -> bool {
        return pow(a.x, 2) + pow(a.y, 2) < pow(b.x, 2) + pow(b.y, 2);
    });

    // For each Pub, check list of good Pubs. If no good Pubs are near,
    // add current Pub to list of good Pubs.
    vector<Pub> good;
    for (const Pub &p : pubs) {
        bool is_good = true;
        for (const Pub &g : good) {
            if (near(p, g)) {
                is_good = false;
                break;
            }
        }
        if (is_good) good.push_back(p);
    }

    // Order good Pubs by id.
    sort(good.begin(), good.end(),
         [](const Pub &a, const Pub &b) -> bool { return a.id < b.id; });

    // Output number of good Pubs, then space separated list of ids in order.
    cout << good.size() << endl;
    // for (const Pub& el : good) cout << el.id << " ";

    cout << endl << (double)(clock() - tStart) / CLOCKS_PER_SEC << " seconds\n";

    return 0;
}