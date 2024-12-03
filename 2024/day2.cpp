#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int treatNumber(vector<int> vec, bool part2){
	bool safe = true, decrease = false, increase = false;
	int counter = 0, thisnum = 0, prev = 0, returnValue = 0, part2extra = 0;

	vector<int> extra;

    for (int thisnum : vec) {
		cout << thisnum << " ";
        counter++;
		extra.push_back(thisnum);
		if (!safe){
			continue;
		}
		if (counter == 1) {
			prev = thisnum;
		}
		if (counter == 2) {
			if (prev == thisnum) {
				safe = false;
				extra.erase(extra.end() - 2);
			} else if (prev < thisnum) {
				if (thisnum - prev > 3) {
					safe = false;
					extra.erase(extra.end() - 2);
				} else {
					increase = true;
				}
			} else {
				if (prev - thisnum > 3) {
					safe = false;
					extra.erase(extra.end() - 2);
				} else {
					decrease = true;
				}
			}
			prev = thisnum;
		}
		if (counter > 2) {
			if (decrease) {
				if (prev < thisnum) {
					safe = false;
					extra.pop_back();
				} else if(prev == thisnum){
					safe = false;
					extra.pop_back();
				} else {
					if (prev - thisnum > 3) {
						safe = false;
						extra.pop_back();
					}
				}
			}
			if (increase) {
				if (prev > thisnum) {
					safe = false;
					extra.pop_back();
				} else if(prev == thisnum){
					safe = false;
					extra.pop_back();
				} else {
					if (thisnum - prev > 3) {
						safe = false;
						extra.pop_back();
					}
				}
			}
			prev = thisnum;
		}
    }
	if (safe) {
		returnValue++;
	} else {
		if(part2){
			part2extra += treatNumber(extra, false);
			returnValue += part2extra;
		}
	}
	
	cout << " - safe : " << safe;
	cout << " - part2extra : " << part2extra;
	cout << endl;

	return returnValue;
}

int main() {
	// Create a text string, which is used to output the text file
	string myText;

	// Read from the text file
	ifstream MyReadFile("input.txt");

	int part1res = 0;
	int part2res = 0;
	vector<vector<int>> mainvector;
	
	// Use a while loop together with the getline() function to read the file line by line
	while (getline(MyReadFile, myText)) {
		istringstream iss(myText);
		string token;
		vector<int> vec;
		while (iss >> token) {
			if (!token.empty()) {
				vec.push_back(stoi(token));
			}
		}
		mainvector.push_back(vec);
	}

	for (vector<int> vec : mainvector) {
		part1res += treatNumber(vec, false);
		part2res += treatNumber(vec, true);
	}

	cout << "Part 1: " << part1res << endl;
	cout << "Part 2: " << part2res << endl;

	// Close the file
	MyReadFile.close();
}
