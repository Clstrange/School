#include <iostream>

using namespace std;

void PrintNumPattern(int num1, int num2) {
	static int x = -1;
	static int num1PlaceHolder = num1;
	cout << num1 << " ";
	if (num1 < 1 || num1 == num1PlaceHolder) {
		x += 1;
	};

	if (x == 0) {
		PrintNumPattern((num1 - num2), num2);
	}
	else if(x == 1) {
		PrintNumPattern((num1 + num2), num2);
	}
	else {
		return;
	}

}

int main(int argc, char* argv[]) {
   int num1;
   int num2;

   cin >> num1;
   cin >> num2;
   PrintNumPattern(num1, num2);
   
   return 0;
}