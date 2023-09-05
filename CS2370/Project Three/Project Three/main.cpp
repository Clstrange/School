#include <iostream>
#include "bits.h"

using namespace std;



int main() {

    Bits test;
    test.set(4);
    test.set(3);
    cout << test.ones();
    return 0;

}


