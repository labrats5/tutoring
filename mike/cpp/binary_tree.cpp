#include "binary_tree.h"

int main() {
    int s;
    Tree<int> t = Tree<int>();
    while (cin >> s && s != EOF) { t.insert(s); }
    t.postorder();
    return 0;
}
