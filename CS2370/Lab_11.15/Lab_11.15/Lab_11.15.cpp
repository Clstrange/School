
#include <iostream>
#include <fstream>
using namespace std;



void openFile(string fileName){
    ifstream inFS;
    string data;
    string file;

    inFS.open(fileName);

    if (!inFS.is_open()) {
        cout << "failed" << endl;
        return;
    }

    inFS >> data;


    while (!inFS.eof()) {

        if (data[0] == '@') {
            data.erase(data.begin());
            openFile(data);
            data = '@' + data;
        }
        if (data == fileName || data[0] == '@') {
            inFS >> data;
        }
        else {
            cout << data << endl;
            inFS >> data;
        }
    }
}




int main(int argc, char* argv[]) {
    string fileName;

    cout << "32 items:" << endl << endl;
    for (int i = 1; i < argc; ++i) {
        
        if ((argv[i])[0] == '@') {
            fileName = argv[i];
            fileName.erase(fileName.begin());
            openFile(fileName);
        }
        else {
            cout << argv[i] << endl;
        }
    }
    return 0;
}
