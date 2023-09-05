#include <iostream>
#include <string> 
using namespace std;

int main() {
	int spaceCounter = 0;
	string test;
	string firstName;
	string middleName;
	string lastName;
	string temp;
	int key = 0;
	getline(cin, test);

	for (int i = 0; i < test.size(); i++) {
		if (isspace(test[i])) {
			spaceCounter += 1;
		}
	}

	if (spaceCounter == 1) {
		
		for (int i = 0; i < test.size(); i++) {
			if (key == 1) {
				lastName += test[i];
			}

			if (isspace(test[i])) {
				key = 1;
			}

			if (key == 0) {
				firstName += test[i];
			}
		}


		cout << lastName << ", " << firstName[0] << "." << endl;
	}

	if (spaceCounter == 2) {

		for (int i = 0; i < test.size(); i++) {
			if (key == 1) {

				if (!isspace(test[i])) {
					lastName += test[i];
				}
			}

			if (key == 2) {
				middleName += test[i];
			}
			

			if (isspace(test[i])) {
				if (key == 0) {
					key = 1;
				}
				else {
					key = 2;
				}

			}

			if (key == 0) {
				if (!isspace(test[i])) {
					firstName += test[i];
				}

			}
		}


		cout << middleName << ", " << firstName[0]
			<< "." << lastName[0] << "." << endl;

	}
	return 0;
}