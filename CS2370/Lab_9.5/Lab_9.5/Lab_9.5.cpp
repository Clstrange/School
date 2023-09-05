#include <string>
#include <iostream>

using namespace std;

int main() {
    string inputName;
    string age;
    int intAge;
    // Set exception mask for cin stream
    cin.exceptions(ios::failbit);

    cin >> inputName;

    while (inputName != "-1") {
        // FIXME: The following line will throw an ios_base::failure.
        //        Insert a try/catch statement to catch the exception.
        //        Clear cin's failbit to put cin in a useable state.

        try {
            cin >> age; 

            for (int i = 0; i < age.length(); i++) {
                if (!(isdigit(age[i]))) {
                    throw runtime_error("Incorrect Value");
                }
            }

            intAge = stoi(age);


            cout << inputName << " " << (intAge + 1) << endl;

            cin >> inputName;

        }
        catch (runtime_error excpt) {
            intAge = 0;
            cout << inputName << " " << intAge << endl;
            cin.clear();
            cin.ignore(10000, '\n');
            cin >> inputName;
        }


    }

    return 0;
}