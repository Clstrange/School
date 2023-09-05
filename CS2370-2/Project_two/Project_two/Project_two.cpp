#include <iostream>
#include <string>
using namespace std;
bool key = false;
void PrintMenu() {

	cout << "MENU" << endl
		<< "c - Number of non-whitespace characters" << endl
		<< "w - Number of words" << endl
		<< "f - Find text" << endl
		<< "r - Replace all !'s" << endl
		<< "s - Shorten spaces" << endl
		<< "q - Quit" << endl;

}
int GetNumOfNonWSCharacters(const string& userString) {
	int charCount = 0;
	for (int i = 0; i < userString.size(); i++) {
		if (isspace(userString.at(i))) {

		}
		else {
			charCount += 1;
		}
	}
	return charCount;
}
int GetNumOfWords(const string& userString) {
	bool wordComplete = false;
	int wordCount = 0;
	for (int i = 0; i < userString.size(); i++) {
		if (wordComplete == true) {
			if (!isalpha(userString.at(i)) && userString.at(i) != '\'') {
				wordCount += 1;
				wordComplete = false;
			}
		}
		else {
			if (isalpha(userString.at(i))) {
				wordComplete = true;
			}
			else {
				
			}
		}
	}
	return wordCount;
}
int FindText(string textToFind, const string& userString) {
	int counter = 0;
	int strPos = 0; 
	while (userString.find(textToFind, strPos) < userString.size()) {
		if (userString.find(textToFind, strPos) + textToFind.size() == userString.size() || isalpha(userString.at(userString.find(textToFind, strPos) + textToFind.size()))) {
			if (userString.find(textToFind, strPos) + textToFind.size() == userString.size()) {
				counter += 1;
			}

		}
		else {
			counter += 1;
		}

		strPos = userString.find(textToFind, strPos) + 1;
	}
	return counter;
}
void ReplaceExclamation(string& userString) {
	for (int i = 0; i < userString.size(); i++) {
		if (userString.at(i) == '!') {
			userString.at(i) = '.';
		}
	}
}
void ShortenSpace(string& userString) {
	string newString = "";
	for (int i = 0; i < userString.size(); i++) {
		if (userString.at(i) == ' ') {
			if (userString.at(i + 1) == ' ') {

			}
			else {
				newString += userString.at(i);
			}

		}
		else {
			newString += userString.at(i);
		}
	}
	userString = newString;
}
void ExecuteMenu(char userChar, string& userString) {
	string textToFind;
	while (userChar != 'q') {
		switch (userChar) {
		case 'c':
			cout << "Number of non-whitespace characters: " << GetNumOfNonWSCharacters(userString) << endl;
			cout << endl;
			PrintMenu();
			cout << endl;
			cout << "Choose an option:" << endl;
			cin >> userChar;
			break;
		case 'w':
			cout << "Number of words: " << GetNumOfWords(userString) << endl;
			if (key == true) {
				cout << endl;
				PrintMenu();
				cout << endl;
				cout << "Choose an option:" << endl;
				cin >> userChar;
			}
			else {
				userChar = 'q';
			}
			break;
		case 'f':
			cout << "Enter a word or phrase to be found:" << endl;
			cin.ignore();
			getline(cin, textToFind);
			cout << "\"" << textToFind << "\"" << " instances: " << FindText(textToFind, userString) << endl;
			cout << endl;
			PrintMenu();
			cout << endl;
			cout << "Choose an option:" << endl;
			cin >> userChar;
			break;
		case 'r':
			ReplaceExclamation(userString);
			cout << "Edited text: " << userString << endl;
			cout << endl;
			PrintMenu();
			cout << endl;
			cout << "Choose an option:" << endl;
			cin >> userChar;
			break;
		case 's':
			ShortenSpace(userString);
			cout << "Edited text: " << userString << endl;
			cout << endl;
			PrintMenu();
			cout << endl;
			cout << "Choose an option:" << endl;
			cin >> userChar;
			break;
		case 'q':
			break;
		}
	}

}
int main() {
	key = true;
	string userString;
	char userChar = ' ';
	cout << "Enter a sample text:" << endl;
	getline(cin, userString);
	cout << endl;
	cout << "You entered: " << userString << endl;
	cout << endl;
	PrintMenu();
	cout << endl;
	while (userChar != 'c' && userChar != 'w' && userChar != 'f' && userChar != 'r' && userChar != 's' && userChar != 'q') {
		cout << "Choose an option:" << endl;
		cin >> userChar;
	}
	ExecuteMenu(userChar, userString);
	return 0;
}