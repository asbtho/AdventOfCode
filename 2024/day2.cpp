#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	// Create a text string, which is used to output the text file
	string myText;

	// Read from the text file
	ifstream MyReadFile("input.txt");

	int part1res = 0;
	
	// Use a while loop together with the getline() function to read the file line by line
	while (getline(MyReadFile, myText)) {
		std::istringstream iss(myText);
		std::string token;
		bool part1safe = true, decrease = false, increase = false;
		int counter = 0, thisnum = 0, prev = 0, prevprev = 0, flipCount = 0, equalsCount = 0, largeGapCount = 0;
		while (iss >> token) {
			if (!token.empty()) {
				counter++;
				thisnum = stoi(token);
				if (counter == 1) {
					prev = thisnum;
				}
				if (counter == 2) {
					if (prev == thisnum) {
						equalsCount++;
					} else if (prev < thisnum) {
						if (thisnum - prev > 3) {
							part1safe = false;
							largeGapCount++;
						} else {
							increase = true;
						}
					} else {
						if (prev - thisnum > 3) {
							part1safe = false;
							largeGapCount++;
						} else {
							decrease = true;
						}
					}
					prevprev = prev;
					prev = thisnum;
				}
				if (counter > 2) {
					if (decrease) {
						if (prev < thisnum) {
							part1safe = false;
							flipCount++;
						} else if(prev == thisnum){
							equalsCount++;
						} else {
							if ((prev - thisnum) > 3) {
								part1safe = false;
								largeGapCount++;
							}
						}
					} else if (increase) {
						if (prev > thisnum) {
							part1safe = false;
							flipCount++;
						} else if(prev == thisnum){
							equalsCount++;
						} else {
							if ((thisnum - prev) > 3) {
								part1safe = false;
								largeGapCount++;
							}
						}
					} else {
						if (prev == thisnum) {
							equalsCount++;
						} else if (prev < thisnum) {
							if (thisnum - prev > 3) {
								part1safe = false;
								largeGapCount++;
							}
							else {
								increase = true;
							}
						} else {
							if (prev - thisnum > 3) {
								part1safe = false;
								largeGapCount++;
							}
							else {
								decrease = true;
							}
						}
					}
					prevprev = prev;
					prev = thisnum;
				}
				cout << token << " ";
			}
		}
		if (equalsCount > 0) {
			part1safe = false;
		}
		if (flipCount > 0) {
			part1safe = false;
		}
		if (part1safe) {
			part1res++;
		}
		cout << " part1Safe : " << part1safe;
		cout << " equalsCount : " << equalsCount;
		cout << " flipCount : " << flipCount;
		cout << " largeGapCount : " << largeGapCount;
		cout << endl;
	}

	cout << "Part 1: " << part1res << endl;

	// Close the file
	MyReadFile.close();
}
