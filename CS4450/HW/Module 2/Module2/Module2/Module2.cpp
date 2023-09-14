// Module2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

union Data {

	unsigned long long signedInt64;

	struct
	{
		unsigned int code : 5;
		int ladrm : 4;
		int radrm : 4;
		int si : 7;
		int ireg : 6;
		int rreg : 6;
		int li : 32;
	} nestedStruct;
};

void readStuff(unsigned long long x) {
	Data myData;
	myData.nestedStruct.code = x;
	myData.signedInt64 = x;
	cout << myData.signedInt64;
	cout << endl;
	cout << myData.nestedStruct.code;
}


int main() {
	unsigned long long x;
	while (cin >> hex >> x) {
		cout << "Instruction: " << hex << x << endl;
		cout << dec;      // Convert back to decimal
		readStuff(x);
		cout << endl;
	}
}
