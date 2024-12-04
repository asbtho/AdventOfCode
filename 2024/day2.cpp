#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int treatNumber(vector<int> vec, bool part2, ofstream& outFile){
	bool safe = true, decrease = false, increase = false;
	int counter = 0, thisnum = 0, prev = 0, prevprev = 0, returnValue = 0, part2extra = 0;

	vector<int> extra;

    for (int thisnum : vec) {
		cout << thisnum << " ";
        outFile << thisnum << " ";
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
			prevprev = prev;
			prev = thisnum;
		}
		if (counter == 3) {
			if (decrease) {
				if (prev < thisnum) {
					safe = false;
					extra.erase(extra.end() - 2);
					extra.erase(extra.end() - 2);
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
					extra.erase(extra.end() - 2);
					extra.erase(extra.end() - 2);
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
			prevprev = prev;
			prev = thisnum;
		}
		if (counter > 3) {
			if (decrease) {
				if (prev < thisnum) {
					safe = false;
					if(prevprev > thisnum){
						extra.erase(extra.end() - 2);
					} else {
						extra.pop_back();
					}
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
					if(prevprev < thisnum){
						extra.erase(extra.end() - 2);
					} else {
						extra.pop_back();
					}
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
			prevprev = prev;
			prev = thisnum;
		}
    }
	if (safe) {
		returnValue++;
	}

	cout << " - safe : " << safe << endl;
    outFile << " - safe : " << safe << endl;

	if(part2 && !safe){
		cout << "Running part 2 with one removed:" << endl;
		outFile << "Running part 2 with one removed:" << endl;
		part2extra += treatNumber(extra, false, outFile);
		returnValue += part2extra;
	}

	return returnValue;
}

int main() {
    ofstream outFile("output.txt");
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
		part1res += treatNumber(vec, false, outFile);
		part2res += treatNumber(vec, true, outFile);
	}

	cout << "Part 1: " << part1res << endl;
	outFile << "Part 1: " << part1res << endl;
	cout << "Part 2: " << part2res << endl;
	outFile << "Part 2: " << part2res << endl;

	// Close the file
	MyReadFile.close();
}
