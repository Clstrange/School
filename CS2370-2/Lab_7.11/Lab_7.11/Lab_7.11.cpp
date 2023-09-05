#include <iostream>

using namespace std;

void PrintNumPattern(int num1, int num2) {
	int newNum = num1 - num2;
	cout << num1 << " ";
	if (newNum < 0) {
		cout << newNum << " ";
	}
	if (newNum >= 0) {
		PrintNumPattern(newNum, num2);
	}

	newNum += num2;
	cout << newNum << " ";

}

int main() {
	int num1;
	int num2;

	cin >> num1;
	cin >> num2;
	PrintNumPattern(num1, num2);

	return 0;
}