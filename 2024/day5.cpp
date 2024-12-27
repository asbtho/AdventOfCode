#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
using namespace std;

int main() {
	// Create a text string, which is used to output the text file
	string myText;

	// Read from the text file
	ifstream MyReadFile("input.txt");
	bool parseFirst = true;
	vector<vector<int>> rules;
	vector<vector<int>> updates;

	// Parse lines
	while (getline(MyReadFile, myText)) {
		//cout << myText << endl;
		if (myText == ""){
			cout << "switching" << endl;
			parseFirst = false;
			continue;
		}
		if (parseFirst){
			regex rulesPattern{"(\\d+)(\\|)(\\d+)"};
			sregex_iterator Iterator{myText.begin(), myText.end(), rulesPattern };
			sregex_iterator End;
			while (Iterator != End) {
				smatch results = *Iterator;
				cout << results[1] << "," << results[3] << endl;
				rules.push_back({stoi(results[1]),stoi(results[3])});
				++Iterator;
			}
		} else {
			cout << myText << endl;
			regex updatesPattern{"(\\d+)"};
			sregex_iterator updateIterator{myText.begin(), myText.end(), updatesPattern };
			sregex_iterator updateEnd;
			vector<int> update;
			while (updateIterator != updateEnd) {
				smatch updateResults = *updateIterator;
				cout << updateResults[0] << endl;
				update.push_back(stoi(updateResults[0]));
				++updateIterator;
			}
			updates.push_back(update);
		}
	}

	// Close the file
	MyReadFile.close();
}
