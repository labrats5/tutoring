#include "header_test.h"

#include <iostream>

int addtwo(int a, int b) { return a + b; }
int doubleup(int a) { return a * 2; }

void my_struct::add() { std::cout << x + y << std::endl; }