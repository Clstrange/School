#include <iostream>
#include <string>

using namespace std;

int DateParser(string month) {
	int monthInt = 0;

	if (month == "January")
		monthInt = 1;
	else if (month == "February")
		monthInt = 2;
	else if (month == "March")
		monthInt = 3;
	else if (month == "April")
		monthInt = 4;
	else if (month == "May")
		monthInt = 5;
	else if (month == "June")
		monthInt = 6;
	else if (month == "July")
		monthInt = 7;
	else if (month == "August")
		monthInt = 8;
	else if (month == "September")
		monthInt = 9;
	else if (month == "October")
		monthInt = 10;
	else if (month == "November")
		monthInt = 11;
	else if (month == "December")
		monthInt = 12;
	return monthInt;
}

int main() {
	string month;
	string day;
	string year;
	int newMonth;
	int newDay;
	while (month != "-1") {
		cin >> month;
		if (month != "-1") {
			newMonth = DateParser(month);
			if (newMonth > 0 && newMonth < 13) {
				cin >> day;
				if (day.find(',') != std::string::npos) {
					day.resize(day.size() - 1);
					newDay = stoi(day);
					cin >> year;
					if (newDay >= 1 && newDay <= 31) {
						if (stoi(year) >= 1 && stoi(year) <= 9999) {
							cout << newMonth << "/" << newDay << "/" << year << endl;
						}
					}
				}
			}
		}
	}
}
