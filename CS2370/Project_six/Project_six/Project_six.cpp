// Project_six.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <set>
#include <iterator>
#include <random>
#include <ctime>
#include <string>
#include <tuple>
using namespace std;


struct MyLessString
{
    bool operator () (const string& lhs, const string& rhs) const 
    {
        return make_pair(lhs.length(), lhs) < make_pair(rhs.length(), rhs);
    }
};

bool sort_size(const string word_1, const string word_2) {
    return word_1.size() < word_2.size();
}
int main()
{
    fstream file;
    string test_word;
    string word;
    string end_search;
    vector<string> word_list;
    vector<string> sub_word_list;
    multiset<char> word_set;

    int iterator = 0;


    file.open("words.txt");

    if (!file.is_open()) {
        cout << "File failed to open" << endl;
    }
    while (!file.fail()) {
        file >> test_word;
        if (test_word.size() >= 3) {
            word_list.push_back(test_word);
        }
        
    }
    if (!file.eof()) {
        cout << "Failed to read entire file" << endl;
    }

    sort(word_list.begin(), word_list.end(), sort_size);



    default_random_engine dre(time(nullptr)); // Seed the engine
    uniform_int_distribution<int> di(0, word_list.size());
    int n = di(dre);


    word = word_list.at(n);

    for (char c : word) {
        word_set.insert(c);
    }

    while (word.size() >= end_search.size()) {
        multiset<char> sub_word_set;
        end_search = word_list.at(iterator);

        for (char c : end_search) {
            sub_word_set.insert(c);
        }

        if (includes(word_set.begin(), word_set.end(), sub_word_set.begin(), sub_word_set.end())) {
            sub_word_list.push_back(end_search);
        }
        //else {
        //    cout << "failed" << iterator << endl;
        //}
        iterator += 1;
    }
    cout << "The word is " << word << endl << endl;

    sort(sub_word_list.begin(), sub_word_list.end(), MyLessString{});

    for (int i = 0; i < sub_word_list.size(); i++) {
        
        cout << sub_word_list.at(i) << endl;
    }
}

