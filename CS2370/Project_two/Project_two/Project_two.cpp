#include <iostream>
#include <string>
using namespace std;
string userString; //forced to use this global variable

/* Declaring Functions */
int GetNumOfNonWSCharacters(const string userString);
int FindText(const string userString, const string userText);
int GetNumOfWords(const string userString);
string ReplaceExclamation(string &userString);
string ShortenSpace(string &userString);
void ExecuteMenu(char userChar, string &userString);
void PrintMenu();

/* Main Function */
int main() {
	cout << "Enter a sample text:";
	getline(cin, userString);
	cout << endl << endl;
	cout << "You entered: " << userString << endl;
	PrintMenu();
	return 0;
}
int GetNumOfNonWSCharacters(const string userString) {
	int charCount = 0;
	for (int i = 0; i < userString.length(); ++i) {
		if (isspace(userString[i])) {
		}
		else {
			charCount++;
		}
	}
	return charCount;
}
int GetNumOfWords(const string userString) {
	int wordCount = 1;

	for (int i = 0; i < userString.length(); ++i) {
		if (!(isspace(userString[i]))) {
			if (isspace(userString[i + 1])) {
				wordCount++;
			}
			
		}
	}
	return wordCount;
}
int FindText(string userText, const string userString) {
	int wordCount = 0;
	string tempWord;
	string tempUserText;

	for (int n = 0; n < userText.length(); ++n) {
		if (isalpha(userText[n])) {
			tempUserText = tempUserText + userText[n];

		}
	}
	userText = tempUserText;

	for (int i = 0; i < userString.length(); ++i) {
		while ((isalpha(userString[i])) || (userString[i] == false)) {
			tempWord = tempWord + userString[i];
			i = i + 1;

		}

		for (int x = 0; x < tempWord.length(); ++x) {
			if (tempWord[x] == userText[x]) {
				if (tempWord == userText) {
					wordCount = wordCount + 1;
					tempWord = "";
					break;
				}
			}
			else {
				tempWord = "";
				break;

			}
		}

	}
	return wordCount;
}
string ReplaceExclamation(string &userString) {
	for (int i = 0; i < userString.length(); ++i) {
		if (userString[i] == '!') {
			userString[i] = '.';
		}
	}

	return userString;
}
string ShortenSpace(string &userString) {
	string tempUserString;
	for (int i = 0; i < userString.length(); ++i) {

		if (isspace(userString[i])) {
			if (isspace(userString[i + 1])) {
				continue;
			}
		}
		tempUserString = tempUserString + userString[i];
	}
	userString = tempUserString;
	return userString;
}
void ExecuteMenu(char userChar, string& userString) {
	string userText;

	if (userChar == 'c') {
		cout << "Number of non-whitespace characters: "
			<< GetNumOfNonWSCharacters(userString) << endl;
		PrintMenu();

	}
	else if (userChar == 'w') {
		cout << "Number of words: " 
			<< GetNumOfWords(userString) 
			<< endl;
		PrintMenu();
	}
	else if (userChar == 'f') {
		cout << "Enter a word or phrase to be found:" << endl;
		cin.ignore();
		getline(cin, userText);
		cout << "\"" 
			<< userText 
			<< "\""
			<< " instances: " 
			<< FindText(userText, userString)
			<< endl;
		PrintMenu();
	}
	else if (userChar == 'r') {
		ReplaceExclamation(userString);
		cout << "Edited text: " << userString << endl;
		PrintMenu();
	}
	else if (userChar == 's') {
		ShortenSpace(userString);
		cout << "Edited text: " << userString << endl;
		PrintMenu();
		
	}
	else if (userChar == 'q') {
		return;
	}
	else {
		cout << "Error!!!";
	}
	return;
}
void PrintMenu() {
	char userChar;

	cout << endl
		<< "MENU" << endl
		<< "c - Number of non-whitespace characters" << endl
		<< "w - Number of words" << endl
		<< "f - Find text" << endl
		<< "r - Replace all !'s" << endl
		<< "s - Shorten spaces" << endl
		<< "q - Quit" << endl
		<< endl
		<< "Choose an option:" << endl;

	cin >> userChar;

	if (userChar == 'c' ||
		userChar == 'w' ||
		userChar == 'f' ||
		userChar == 'r' ||
		userChar == 's' ||
		userChar == 'q') {
		ExecuteMenu(userChar, userString);

	}
	else {
		PrintMenu();

	}
	return;
}