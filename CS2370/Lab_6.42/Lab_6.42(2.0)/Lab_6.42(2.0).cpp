#include <iostream>
#include <vector> 
#include <string>
using namespace std;

int GetFrequencyOfWord(vector<string> wordsList, string currWord) {


	int stackNum;
	for (int firstWord = 0; firstWord < wordsList.size(); ++firstWord) {
		stackNum = 0;
		for (int secondWord = 0; secondWord < wordsList.size(); ++secondWord) {
			if (wordsList.at(firstWord) == wordsList.at(secondWord)) {
				stackNum = stackNum + 1;

			}
		}
		cout << wordsList.at(firstWord) << " " << stackNum << endl;
	}


	return 0;

}

int main() {
	string currWord;
	int wordCount;
	cin >> wordCount;
	vector<string> wordList(wordCount);
	
	for (int i = 0; i < wordCount; ++i) {
		cin >> currWord;
		wordList.at(i) = newWord;
	}

	GetFrequencyOfWord(wordList, "hello");

	return 0;
}