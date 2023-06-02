#include <iostream>
#include <cstdlib>

using namespace std;

int* merge(int* a, int m, int* b, int n) {
    int i = 0, j = 0, k = 0;
    int* c = (int*)malloc((m+n) * sizeof(int));
    while (i < m && j < n) {
        if (a[i] < b[j]) {
            c[k++] = a[i++];
        }
        else {
            c[k++] = b[j++];
        }
    }
    while (i < m) {
        c[k++] = a[i++];
    }
    while (j < n) {
        c[k++] = b[j++];
    }

    return c;
}

int main() {
    int a[5] = {1, 3, 5, 7, 9};
    int b[5] = {2, 4, 6, 8, 10};
    int* c = merge(a, 5, b, 5);
    for (int i = 0; i < 10; i++) {
        cout << c[i] << endl;
    }
    return 0;
}