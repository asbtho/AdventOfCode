#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
using namespace std;

void parseUpdates(vector<vector<int>> &rules, vector<vector<int>> &updates){
	int count = 0;
	for(vector<int> update : updates){
		bool valid = true;
		for(vector<int> rule : rules){
			vector<int> temp;
			for(int num : update){
				if(num == rule[0] || num == rule[1]){
					temp.push_back(num);
				}
			}
			if(temp.size() == 2){
				if(temp != rule){
					valid = false;
				}
			}
		}
		if(valid){
			auto middle = update.begin() + update.size() / 2;
			count += *(middle);
		}
	}
	cout << "COUNT IS: " << count << endl;
}

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
			//cout << "switching" << endl;
			parseFirst = false;
			continue;
		}
		if (parseFirst){
			regex rulesPattern{"(\\d+)(\\|)(\\d+)"};
			sregex_iterator Iterator{myText.begin(), myText.end(), rulesPattern };
			sregex_iterator End;
			while (Iterator != End) {
				smatch results = *Iterator;
				//cout << results[1] << "," << results[3] << endl;
				rules.push_back({stoi(results[1]),stoi(results[3])});
				++Iterator;
			}
		} else {
			//cout << myText << endl;
			regex updatesPattern{"(\\d+)"};
			sregex_iterator updateIterator{myText.begin(), myText.end(), updatesPattern };
			sregex_iterator updateEnd;
			vector<int> update;
			while (updateIterator != updateEnd) {
				smatch updateResults = *updateIterator;
				//cout << updateResults[0] << endl;
				update.push_back(stoi(updateResults[0]));
				++updateIterator;
			}
			updates.push_back(update);
		}
	}

	parseUpdates(rules, updates);

	// Close the file
	MyReadFile.close();
}
