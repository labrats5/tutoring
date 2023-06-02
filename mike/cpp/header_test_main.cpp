#include <iostream>

#include "header_test.h"

int main() {
    my_struct c = {4, 5};
    std::cout << addtwo(3, 5) << " " << std::endl;
    c.add();
    return 0;
}