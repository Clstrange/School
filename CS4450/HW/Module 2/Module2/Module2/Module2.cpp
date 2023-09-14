// Module2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

union Data {

	unsigned long long signedInt64;

	struct
	{
		int li : 32;
		int rreg : 6;
		int ireg : 6;
		int si : 7;
		int radrm : 4;
		int ladrm : 4;
		int code : 5;
	} nestedStruct;
};

void readStuff(unsigned long long x) {
	Data myData;
	myData.nestedStruct.code = x;
	myData.nestedStruct.ladrm = x;
	myData.nestedStruct.radrm = x;
	myData.nestedStruct.si = x;
	myData.nestedStruct.ireg = x;
	myData.nestedStruct.rreg = x;
	myData.nestedStruct.li = x;
	myData.signedInt64 = x;
	cout << myData.signedInt64;
	cout << endl;
	cout << myData.nestedStruct.code;
	cout << endl;
	cout << myData.nestedStruct.ladrm;
	cout << endl;
	cout << myData.nestedStruct.radrm;
	cout << endl;
	cout << myData.nestedStruct.si;
	cout << endl;
	cout << myData.nestedStruct.ireg;
	cout << endl;
	cout << myData.nestedStruct.rreg;
	cout << endl;
	cout << myData.nestedStruct.li;

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
