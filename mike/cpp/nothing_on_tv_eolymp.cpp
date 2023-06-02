#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <tuple>
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

// override cout << for Pub.
ostream &operator<<(ostream &out, const Pub &p) {
    out << "id: " << p.id << "\tx: " << p.x << "\ty: " << p.y
        << "\tdir: " << p.dir;
    return out;
}

using namespace std;

struct Node {
    Pub value;
    Node *left, *right;

    Node(Pub data) : value(data), left(nullptr), right(nullptr) {}
};

Node *CreateNode(Pub data) {
    Node *newNode = new Node(data);
    return newNode;
}

void preorderNode(Node *root) {
    if (!root) return;
    std::cout << root->value << std::endl;
    preorderNode(root->left);
    preorderNode(root->right);
}

void inorderNode(Node *root) {
    if (!root) return;
    inorderNode(root->left);
    std::cout << root->value << std::endl;
    inorderNode(root->right);
}

void postorderNode(Node *root) {
    if (!root) return;
    postorderNode(root->left);
    postorderNode(root->right);
    std::cout << root->value << std::endl;
}

void nodeToVector(Node *root, vector<Pub> &vec) {
    if (!root) return;
    nodeToVector(root->left, vec);
    vec.push_back(root->value);
    nodeToVector(root->right, vec);
}

Node *searchNode(Node *root, Pub val) {
    if (!root || val == root->value) {
        return root;
    }
    if (val < root->value) {
        return searchNode(root->left, val);
    }
    return searchNode(root->right, val);
}

pair<Node *, bool> insertNode(Node *&root, Pub data) {
    if (!root) {
        root = new Node(data);
        return make_pair(root, true);
    }
    if (data == root->value) {
        return make_pair(root, false);
    }
    if (data < root->value) {
        if (!root->left) {
            root->left = new Node(data);
            return make_pair(root->left, true);
        }
        return insertNode(root->left, data);
    }
    if (!root->right) {
        root->right = new Node(data);
        return make_pair(root->right, true);
    }
    return insertNode(root->right, data);
}

Node *smallest(Node *root) {
    if (!root || !root->left) {
        return root;
    }
    return smallest(root->left);
}

Node *greatest(Node *root) {
    if (!root || !root->right) {
        return root;
    }
    return greatest(root->right);
}

Node *bisect_left(Node *root, Pub val, Node *curr = nullptr) {
    if (!root || val == root->value) {
        return curr;
    }
    if (val < root->value) {
        return bisect_left(root->left, val, curr);
    }
    curr = root;
    return bisect_left(root->right, val, curr);
}

Node *bisect_right(Node *root, Pub val, Node *curr = nullptr) {
    if (!root || val == root->value) {
        return curr;
    }
    if (root->value < val) {
        return bisect_right(root->right, val, curr);
    }
    curr = root;
    return bisect_right(root->left, val, curr);
}

pair<Node *, bool> deleteNode(Node *root, Pub key) {
    // base case
    bool deleted = false;
    if (!root) return make_pair(root, deleted);

    // If the key to be deleted is
    // smaller than the root's
    // key, then it lies in left subtree
    if (key < root->value) {
        tie(root->left, deleted) = deleteNode(root->left, key);
    }
    // If the key to be deleted is
    // greater than the root's
    // key, then it lies in right subtree
    else if (key > root->value) {
        tie(root->right, deleted) = deleteNode(root->right, key);
    }
    // if key is same as root's key, then This is the node
    // to be deleted
    else {
        // node has no child
        if (!root->left && !root->right) {
            delete root;
            root = nullptr;
            deleted = true;
        }

        // node with only one child
        else if (!root->left) {
            Node *temp = root;
            root = root->right;
            delete temp;
            deleted = true;
        } else if (!root->right) {
            Node *temp = root;
            root = root->left;
            delete temp;
            deleted = true;
        } else {
            // node with two children: Get the inorder successor
            // (smallest in the right subtree)
            Node *temp = smallest(root->right);

            // Copy the inorder successor's content to this node
            root->value = temp->value;

            // Delete the inorder successor
            tie(root->right, deleted) = deleteNode(root->right, temp->value);
        }
    }
    return make_pair(root, deleted);
}

struct Tree {
    Node *root;
    int size = 0;

    void preorder() { preorderNode(root); }
    void inorder() { inorderNode(root); }
    void postorder() { postorderNode(root); }
    void to_vector(vector<Pub> &vec) { nodeToVector(root, vec); }
    Node *lower_bound(Pub val) { return bisect_left(root, val); }
    Node *upper_bound(Pub val) { return bisect_right(root, val); }
    Node *front() { return smallest(root); }
    Node *back() { return greatest(root); }
    Node *search(Pub val) { return searchNode(root, val); }
    pair<Node *, bool> insert(Pub data) {
        pair<Node *, bool> pair = insertNode(root, data);
        if (pair.second) size++;
        return pair;
    }
    bool erase(Pub key) {
        bool erased = deleteNode(root, key).second;
        if (erased) size--;
        return erased;
    }
};
// Calculate if Pub b is within the circle defined by origin and Pub a.
bool near(const Pub &a, const Pub &b) {
    double cx, cy, rsq;
    cx = a.x / 2.0;
    cy = a.y / 2.0;
    rsq = pow(cx, 2) + pow(cy, 2);
    return pow(b.x - cx, 2) + pow(b.y - cy, 2) <= rsq;
}

int main() {
    int i, x, y, N;
    cin >> N;
    // Vector to store all Pubs.
    vector<Pub> pubs;
    pubs.reserve(N);
    for (i = 0; i < N; ++i) {
        cin >> x >> y;
        pubs.push_back(Pub(i + 1, x, y));
    }

    // Order Pubs by distance from origin.
    std::sort(pubs.begin(), pubs.end(), [](const Pub &a, const Pub &b) -> bool {
        return pow(a.x, 2) + pow(a.y, 2) < pow(b.x, 2) + pow(b.y, 2);
    });

    // Closest element to origin is guaranteed good Pub.
    Tree t = Tree();
    Node *left, *right;
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

    return 0;
}