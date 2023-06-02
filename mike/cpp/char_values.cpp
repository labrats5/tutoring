#include <iostream>
#include <bitset>

using namespace std;

void tobinary(unsigned number){
   if (number > 1)
      tobinary(number/2);
   cout << number % 2;
}

int main() {
    // char my_char = '0';
    // std::cout << (int)my_char << std::endl;
    // int x = 3;
    // cout << "x: " << x << " binary: ";
    // tobinary(x);
    // cout << endl;
    // x <<= 5;
    // cout << "x: " << x << " binary: ";
    // tobinary(x);
    // cout << endl;
    // bitset<16> y(x);
    // cout << "y: " << y << endl;
    cout << (char)('0' + 'F') << endl;

    return 0;
}