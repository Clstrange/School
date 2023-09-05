#include "split.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
	string s = "715608,Vergil Heelis,61070 Marcy Park,Fort Worth,TX,76115,682-583-
		7160, vheelis4@blogger.com";
		auto fields = split(s, ',');
	for (const auto& fld : fields)
		cout << fld << endl;
	cout << endl;
}
/* Output:
715608
Vergil Heelis
61070 Marcy Park
Fort Worth
TX
76115
682-583-7160
vheelis4@blogger.com
*/
