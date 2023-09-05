#include <iostream>
using namespace std;

int main() {
	int highwayNumber;
	int highwayDirection;
	cin >> highwayNumber;
	highwayDirection = highwayNumber % 2;

	if (highwayNumber < 100 && highwayNumber > 0) {
		cout << "I-" << highwayNumber << " is primary, going";
		if (highwayDirection == 0) {
			cout << " east/west." << endl;
		}
		else {
			cout << " north/south." << endl;
		}
	}
	else if (highwayNumber < 1000 && ((highwayNumber % 100) != 0) ) {
		cout << "I-" << highwayNumber << " is auxiliary, serving \
I-" << highwayNumber % 100 << ", going";
		if (highwayDirection == 0) {
			cout << " east/west." << endl;
		}
		else {
			cout << " north/south." << endl;
		}
	}
	else {
		cout << highwayNumber << " is not a valid interstate highway number." << endl;
	}

	return 0;
}
