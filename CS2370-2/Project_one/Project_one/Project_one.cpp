
#include <iostream>
#include <vector>
using namespace std;

void AddPlayer(vector<int>& jerseyList, vector<int>& ratingList) {
	int jerseyNumber;
	int ratingNumber;

	cout << "Enter a new player's jersey number:" << endl;
	cin >> jerseyNumber;
	cout << "Enter the player's rating:" << endl << endl;
	cin >> ratingNumber;

	jerseyList.push_back(jerseyNumber);
	ratingList.push_back(ratingNumber);
}

void OutputRoster(vector<int>& jerseyList,vector<int>& ratingList) {
	cout << "ROSTER" << endl;
	for (int i = 0; i < jerseyList.size(); i++) {
		cout << "Player " << i + 1 << " -- Jersey number: " << jerseyList.at(i) << ", Rating: " << ratingList.at(i) << endl;
	}
	cout << endl;
}

void DeletePlayer(vector<int>& jerseyList, vector<int>& ratingList) {
	int jerseyNumber;
	cout << "Enter a jersey number:" << endl;
	cin >> jerseyNumber;
	for (int i = 0; i < jerseyList.size(); i++) {
		if (jerseyList.at(i) == jerseyNumber) {
			jerseyList.erase(jerseyList.begin() + i);
			ratingList.erase(ratingList.begin() + i);
		}

	}

}

void UpdatePlayerRating(vector<int>& jerseyList, vector<int>& ratingList) {
	int jerseyNumber;
	int newJerseyNumber;

	cout << "Enter a jersey number:" << endl;
	cin >> jerseyNumber;
	cout << "Enter a new rating for player:" << endl;
	cin >> newJerseyNumber;

	for (int i = 0; i < jerseyList.size(); i++) {
		if (jerseyList.at(i) == jerseyNumber) {
			ratingList.at(i) = newJerseyNumber;
		}
	}

}

void OutputPlayerAboveARating(vector<int>& jerseyList, vector<int>& ratingList){
	int ratingNumber;
	cout << "Enter a rating:" << endl << endl;
	cin >> ratingNumber;
	cout << "ABOVE " << ratingNumber << endl;

	for (int i = 0; i < jerseyList.size(); i++) {
		if (ratingList.at(i) > ratingNumber) {
			cout << "Player " << i + 1 << " -- Jersey number: " 
				<< jerseyList.at(i) << ", Rating: " 
				<< ratingList.at(i) << endl;
		}
	}
	cout << endl;

}

void Menu(vector<int>& jerseyList, vector<int>& ratingList) {
	/*print out a menue of actions for the user to use
	to alter the team roster*/

	char  menuOption = 'z';
	while (menuOption != 'q') {
		cout << "MENU" << endl
			<< "a - Add player" << endl
			<< "d - Remove player" << endl
			<< "u - Update player rating" << endl
			<< "r - Output players above a rating" << endl
			<< "o - Output roster" << endl
			<< "q - Quit" << endl << endl;
		cout << "Choose an option:" << endl;
		cin >> menuOption;
		switch (menuOption) {
		case 'a':
			AddPlayer(jerseyList, ratingList);
			break;
		case 'd':
			DeletePlayer(jerseyList, ratingList);
			break;
		case 'u':
			UpdatePlayerRating(jerseyList, ratingList);
			break;
		case 'r':
			OutputPlayerAboveARating(jerseyList, ratingList);
			break;
		case 'o':
			OutputRoster(jerseyList, ratingList);
			break;
		case 'q':
			break;
		}
	}
}

int main()
{
	vector<int> jerseyList;
	vector<int> ratingList;
	int jerseyNumber;
	int ratingNumber;

	for (int i = 1; i <= 5; i++) {
		cout << "Enter player " << i << "'s jersey number:" << endl;
		cin >> jerseyNumber;
		jerseyList.push_back(jerseyNumber);
		cout << "Enter player " << i << "'s rating:" << endl;
		cin >> ratingNumber;
		ratingList.push_back(ratingNumber);
		cout << endl;
	}
	OutputRoster(jerseyList, ratingList);
	Menu(jerseyList, ratingList);
}

