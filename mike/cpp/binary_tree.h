#ifndef BINARY_TREE_H
#define BINARY_TREE_H

#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

template <typename T>
struct Node {
    T value;
    Node *left, *right;

    Node(T data) : value(data), left(nullptr), right(nullptr) {}
  
    ~Node() {
        if (left) delete left;
        if (right) delete right;
    }
};

template <typename T>
Node<T> *CreateNode(T data) {
    Node<T> *newNode = new Node<T>(data);
    return newNode;
}

template <typename T>
void preorderNode(Node<T> *root) {
    if (!root) return;
    std::cout << root->value << std::endl;
    preorderNode(root->left);
    preorderNode(root->right);
}

template <typename T>
void inorderNode(Node<T> *root) {
    if (!root) return;
    inorderNode(root->left);
    std::cout << root->value << std::endl;
    inorderNode(root->right);
}

template <typename T>
void postorderNode(Node<T> *root) {
    if (!root) return;
    postorderNode(root->left);
    postorderNode(root->right);
    std::cout << root->value << std::endl;
}

template <typename T>
void nodeToVector(Node<T> *root, vector<T> &vec) {
    if (!root) return;
    nodeToVector(root->left, vec);
    vec.push_back(root->value);
    nodeToVector(root->right, vec);
}

template <typename T>
Node<T> *searchNode(Node<T> *root, T val) {
    if (!root || val == root->value) {
        return root;
    }
    if (val < root->value) {
        return searchNode(root->left, val);
    }
    return searchNode(root->right, val);
}

template <typename T>
pair<Node<T> *, bool> insertNode(Node<T> *&root, T data) {
    if (!root) {
        root = new Node<T>(data);
        return make_pair(root, true);
    }
    if (data == root->value) {
        return make_pair(root, false);
    }
    if (data < root->value) {
        if (!root->left) {
            root->left = new Node<T>(data);
            return make_pair(root->left, true);
        }
        return insertNode(root->left, data);
    }
    if (!root->right) {
        root->right = new Node<T>(data);
        return make_pair(root->right, true);
    }
    return insertNode(root->right, data);
}

template <typename T>
Node<T> *smallest(Node<T> *root) {
    if (!root || !root->left) {
        return root;
    }
    return smallest(root->left);
}

template <typename T>
Node<T> *greatest(Node<T> *root) {
    if (!root || !root->right) {
        return root;
    }
    return greatest(root->right);
}

template <typename T>
Node<T> *bisect_left(Node<T> *root, T val, Node<T> *curr = nullptr) {
    if (!root || val == root->value) {
        return curr;
    }
    if (val < root->value) {
        return bisect_left(root->left, val, curr);
    }
    curr = root;
    return bisect_left(root->right, val, curr);
}

template <typename T>
Node<T> *bisect_right(Node<T> *root, T val, Node<T> *curr = nullptr) {
    if (!root || val == root->value) {
        return curr;
    }
    if (root->value < val) {
        return bisect_right(root->right, val, curr);
    }
    curr = root;
    return bisect_right(root->left, val, curr);
}

template <typename T>
pair<Node<T> *, bool> deleteNode(Node<T> *root, T key) {
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
            Node<T> *temp = root;
            root = root->right;
            delete temp;
            deleted = true;
        } else if (!root->right) {
            Node<T> *temp = root;
            root = root->left;
            delete temp;
            deleted = true;
        } else {
            // node with two children: Get the inorder successor
            // (smallest in the right subtree)
            Node<T> *temp = smallest(root->right);

            // Copy the inorder successor's content to this node
            root->value = temp->value;

            // Delete the inorder successor
            tie(root->right, deleted) = deleteNode(root->right, temp->value);
        }
    }
    return make_pair(root, deleted);
}

template <typename T>
struct Tree {
    Node<T> *root;
    int size = 0;
    
    void preorder() { preorderNode(root); }
    void inorder() { inorderNode(root); }
    void postorder() { postorderNode(root); }
    void to_vector(vector<T> &vec) { nodeToVector(root, vec); }
    vector<T> &to_vector() {
        vector<T> *vec = new vector<T>();
        nodeToVector(root, *vec);
        return *vec;
    }
    Node<T> *lower_bound(T val) { return bisect_left(root, val); }
    Node<T> *upper_bound(T val) { return bisect_right(root, val); }
    Node<T> *front() { return smallest(root); }
    Node<T> *back() { return greatest(root); }
    Node<T> *search(T val) { return searchNode(root, val); }
    pair<Node<T> *, bool> insert(T data) {
        pair<Node<T> *, bool> pair = insertNode(root, data);
        if (pair.second) size++;
        return pair;
    }
    bool erase(T key) {
        bool erased = deleteNode(root, key).second;
        if (erased) size--;
        return erased;
    }
};

#endif // BINARY_TREE_H