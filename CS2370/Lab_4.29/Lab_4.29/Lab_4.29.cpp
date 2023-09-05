#include <iostream>
using namespace std;

int main() {
    int base_height;
    int base_width;
    int head_width;

    cout << "Enter arrow base height:" << endl;
    cin >> base_height;

    cout << "Enter arrow base width:" << endl;
    cin >> base_width;

    cout << "Enter arrow head width:" << endl;
    cin >> head_width;

    while (head_width <= base_width) {
        cout << "Enter arrow head width:" << endl;
        cin >> head_width;
    }


    cout << endl;

    for (int i = 0; i < base_height; i++) {
        for (int n = 0; n < base_width; n++) {
            cout << "*";
        }
        cout << endl;
    }

    for (int i = head_width; i > 0; i--) {
        for (int n = i; n > 0; n--) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}