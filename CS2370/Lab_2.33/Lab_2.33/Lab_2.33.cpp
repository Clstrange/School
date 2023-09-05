#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main() {
	double long r = pow(2.0, (1.0 / 12.0));
	

	int keyFreq;

	cin >> keyFreq;
	cout << fixed << setprecision(2);
	cout << float(keyFreq) << " " << keyFreq * r << " " << keyFreq * pow(r, 2) << " " << keyFreq * pow(r, 3) << " " << keyFreq * pow(r, 4) << endl;

	

	return 0;
}