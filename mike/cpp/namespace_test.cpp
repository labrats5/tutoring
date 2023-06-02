#include <iostream>

namespace A {
    int add(int a, int b) { return a + b; }
    void print() { std::cout << "this is namespace A." << std::endl; }
}

namespace B {
    float add(float a, float b) { return a + b;}
    void print() { std::cout << "this is namespace B." << std::endl; }
}

int main() {
    std::cout << A::add(3, 5) << " " << B::add(4.0, 7.8) << std::endl;
    A::print();
    B::print();
    return 0;
}
