#include <iostream>
#include<vector>
using namespace std;
char userChoice;


/*
Prompt the user to input five pairs of numbers:
A player's jersey number (0 - 99) and the player's rating (1 - 9).
Store the jersey numbers in one int vector
and the ratings in another int vector.
*/

void createRoster(vector<int>& jerseyLyst, vector<int>& ratingLyst) {

	int playerNum;
	int jerseyNum;
	int ratingNum;


	for (int i = 0; i < 5; ++i) {

		playerNum = i + 1;

		cout << "Enter player " << playerNum << "'s jersey number:" << endl;
		cin >> jerseyNum;
		cout << "Enter player " << playerNum << "'s rating:" << endl << endl;
		cin >> ratingNum;

		jerseyLyst.push_back(jerseyNum);
		ratingLyst.push_back(ratingNum);
	}

	cout << "ROSTER" << endl;

	for (int rosterPlayers = 0; rosterPlayers < 5; ++rosterPlayers) {
		playerNum = rosterPlayers + 1;
		cout << "Player " << playerNum << " -- Jersey number: "
			<< jerseyLyst.at(rosterPlayers) << ", "
			<< "Rating: " << ratingLyst.at(rosterPlayers) << endl;
	}
}

/*
Prompt the user for a new player's jersey number and rating.
Append the values to the two vectors.
*/

void addPlayer(vector<int>& jerseyLyst, vector<int>& ratingLyst) {

	int newJersey;
	int newRating;

	cout << "Enter a new player's jersey number:" << endl;
	cin >> newJersey;
	cout << "Enter the player's rating:" << endl;
	cin >> newRating;

	jerseyLyst.push_back(newJersey);
	ratingLyst.push_back(newRating);

}


/*
Prompt the user for a player's jersey number.
Remove the player from the roster.
*/

void deletePlayer(vector<int>& jerseyLyst, vector<int>& ratingLyst) {
	int removeJersey;


	cout << "Enter a jersey number:";

	cin >> removeJersey;
	for (int i = 0; i < jerseyLyst.size(); ++i) {

		if (jerseyLyst.at(i) == removeJersey) {
			jerseyLyst.erase(jerseyLyst.begin() + i);
			break;

		}




	}
	
}

/*
Prompt the user for a player's jersey number.
Prompt again for a new rating for the player,
and then change that player's rating.
*/

void updatePlayer(vector<int>& jerseyLyst, vector<int>& ratingLyst) {

	int upJersey;
	int upRating;

	cout << "Enter a jersey number:" << endl;
	cin >> upJersey;
	cout << "Enter a new rating for player:" << endl;
	cin >> upRating;

	for (int i = 0; i < jerseyLyst.size(); ++i) {

		if (jerseyLyst.at(i) == upJersey) {
			ratingLyst.at(i) = upRating;
			break;
		}
	}

}

/*
Prompt the user for a rating.
Print the jersey number and rating for
all players with ratings above the entered value.
*/

void outputRating(vector<int>& jerseyLyst, vector<int>& ratingLyst) {
	int aboveRating;

	cout << "Enter a rating" << endl;
	cin >> aboveRating;
	cout << "ABOVE " << aboveRating << endl;

	for (int i = 0; i < jerseyLyst.size(); ++i) {
		if (ratingLyst.at(i) > aboveRating) {
			cout << "Player " << i + 1 << " -- Jersey number: "
				<< jerseyLyst.at(i) << ", Rating: " << ratingLyst.at(i) << endl;

		}
	}
}

void outputRoster(vector<int>& jerseyLyst, vector<int>& ratingLyst) {
	cout << "ROSTER" << endl;
	for (int i = 0; i < jerseyLyst.size(); ++i) {
		cout << "Player " << i + 1 << " -- Jersey number: "
			<< jerseyLyst.at(i) << ", Rating: " << ratingLyst.at(i) << endl;


	}
}



/*
Program will store roster and
rating information for a soccer team.
Coaches rate players during tryouts
to ensure a balanced team.
*/

int main() {

	vector<int> jerseyLyst;
	vector<int> ratingLyst;


	createRoster(jerseyLyst, ratingLyst);

	while (userChoice != 'q') {

		cout << endl << "MENU" << endl
			<< "a - Add player" << endl
			<< "d - Remove player" << endl
			<< "u - Update player rating" << endl
			<< "r - Output players above a rating" << endl
			<< "o - Output roster" << endl
			<< "q - Quit" << endl << endl
			<< "Choose an option:" << endl;
		cin >> userChoice;

		if (userChoice == 'a') {
			addPlayer(jerseyLyst, ratingLyst);
		}

		if (userChoice == 'd') {
			deletePlayer(jerseyLyst, ratingLyst);
		}

		if (userChoice == 'u') {
			updatePlayer(jerseyLyst, ratingLyst);
		}

		if (userChoice == 'r') {
			outputRating(jerseyLyst, ratingLyst);

		}

		if (userChoice == 'o') {
			outputRoster(jerseyLyst, ratingLyst);

		}

	}




	return 0;
}