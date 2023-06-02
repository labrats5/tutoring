#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    int i, n, m, animal;
    unordered_map<int, int> mutants;
    cin >> n;
    mutants.reserve(n);
    for (i = 0; i < n; i++) {
        cin >> animal;
        mutants[animal]++;
    }
    cin >> m;
    for (i = 0; i < m; i++) {
        cin >> animal;
        cout << mutants[animal] << endl;
    }
    return 0;
}