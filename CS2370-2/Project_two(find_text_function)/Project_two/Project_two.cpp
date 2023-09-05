#include <iostream>
#include <string>
using namespace std;

/* Define your functions here. */

int main() {

	string test = "Hello hi Hellos, HiOP oweif weo Hello";
	string testTwo = "Hello";

	int counter = 0;
	int testCounter = 0;


	while (test.find(testTwo, testCounter) < test.size()) {

		if (test.find(testTwo, testCounter) + testTwo.size() == test.size() || isalpha(test.at(test.find(testTwo, testCounter) + testTwo.size()))) {
			if (test.find(testTwo, testCounter) + testTwo.size() == test.size()) {
				counter += 1;
			}

		}
		else {
			counter += 1;
		}

		testCounter = test.find(testTwo, testCounter) + 1;		
	}

	return counter;
}