#include <iostream>
#include <vector> 
#include <string>
#include <cctype>
using namespace std;

void GetWordFrequency(vector<string>& wordList, int vectorSize) {

	for (int i = 0; i < vectorSize; i++) {
		int wordCount = 0;
		string currWord = wordList.at(i);

		for (int j = 0; j < vectorSize; j++) {
			string tempWord = wordList.at(j);
			string tempWord2 = currWord;
			tempWord[0] = tolower(tempWord[0]);
			tempWord2[0] = tolower(currWord[0]);

			if (tempWord == tempWord2) {
				wordCount += 1;
			}
		}
		cout << currWord << " " << wordCount << endl;
	}
}

int main() {
	int vectorSize;
	string newWord;
	cin >> vectorSize;
	vector<string> wordList;
	for (int i = 0; i < vectorSize; i++) {
		cin >> newWord;
		wordList.push_back(newWord);
	}
	GetWordFrequency(wordList, vectorSize);

	return 0;
}
