#include <bitset>
#include <iostream>
using namespace std;

int main() {
    cout << "Enter the integer that holds the bits: ";
    unsigned int n;
    cin >> n;


    cout << "Enter the rightmost bit position: ";
    unsigned int k;
    cin >> k;

    cout << "Enter the leftmost bit position: ";
    unsigned int m;
    cin >> m;

    unsigned int mask = 1 << (m - k) - 1;
    mask <<= k;

    unsigned int temp = n & mask;
    unsigned result = temp >> k;


    cout << "Extracting bits " 
        << k << " through " << m 
        << " from " << n << " = " << bitset<32>(n)
        << ":" << result << " = " << temp << endl;
}