#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

struct Point {
    int x, y;

    Point(int _x, int _y) : x(_x), y(_y) {}
};

struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int data) : data(data), left(nullptr), right(nullptr) {}
    ~Node() {
        if (left) delete left;
        if (right) delete right;
    }
};

ostream &operator<<(ostream &out, Node &p) {
    out << "data: " << p.data << "\tleft: " << p.left << "\tright: " << p.right
        << endl;
    return out;
}

int main() {
    // cout << endl;
    // Node *n = new Node(3);
    // Node *l = new Node(1);
    // Node *r = new Node(5);
    // n->left = l;
    // n->right = r;

    // cout << " node pointer " << n << "\nnode value " << *n << "\nnode pointer
    // left " << (*n).left << "\nnode pointer left " << n->left << endl
    //      << "node value " << *(n->left) << endl;
    //           0  1  2  3  4   5   6   7   8   9

    int a[10] = {73, 72, 78, 79, 111, 118, 119, 121, 122, 100};
    int *b = (int *)malloc(10 * sizeof(int));
    vector<int> c;
    for (int i=0; i<10; i++) { c.push_back(a[i]); }
    for (int i=0; i<10; i++) { b[i] = a[i]; }
    cout << a << " " << &a << " " << *a << "\t" << a+1 << " " << *(a+9) << endl;
    cout << b << " " << &b << " " << *b << "\t" << b+1 << " " << *(b+9) << endl;
    cout << &c << " " << c[9] << "\t\t" << &(*c.begin()) << "\t" << *(c.begin()+9) << endl; 

    // int x = 5;
    // int &y = x;
    // int *z;
    // z = &x;

    // cout << "variable\tvalue\t\taddress" << endl;
    // cout << "x:\t\t" << x << "\t\t" << &x << endl;
    // cout << "y:\t\t" << y << "\t\t" << &y << endl;
    // cout << "z:\t\t" << z << "\t" << &z << endl; // "\t" << *z << endl;

    // Point p1(3, 5);

    // Point *p2 = new Point(3, 5);

    // cout << (*p2).x << endl;
    // cout << p2->x << endl;

    // Point *p2 = new Point(8, 17);
    // cout << (*p2).x << endl;
    // cout << p2->x << endl;

    return 0;
}

/*
value       |     17        | 0x16d26b488   |
address     | 0x16d26b488   | 0x16d26b478   |
variable    |     x         |      z        |
*/