#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {

	string userWord;
	string preUserWord;
	string paliWord;

	getline(cin, preUserWord);

	for (int i = 0; i < preUserWord.size(); i++) {
		if (isspace(preUserWord.at(i))) {

		}
		else {
			userWord += preUserWord.at(i);
		}

	}

	for (int i = 1; i <= userWord.size(); i++) {
		paliWord += userWord.at(userWord.size() - i);
	}

	if (paliWord == userWord) {
		cout << "palindrome: " << preUserWord << endl;
	}
	else {
		cout << "not a palindrome: " << preUserWord << endl;
	}

	return 0;
}
