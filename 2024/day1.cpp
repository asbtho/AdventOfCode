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

	// Vectors for numbers
	vector<int> vecLeft;
	vector<int> vecRight;

	int thisnum = 0, count = 0, diffres = 0, simres = 0;

	// Parse lines
	while (getline(MyReadFile, myText)) {
		std::istringstream iss(myText);
		std::string token;
		while (iss >> token) {
			if (!token.empty()) {
				count += 1;
				thisnum = stoi(token);
				if (count % 2 == 0) {
					vecRight.push_back(thisnum);
				} else {
					vecLeft.push_back(thisnum);
				}
			}
		}
	}

	// Sort vectors
	sort(vecLeft.begin(), vecLeft.end());
	sort(vecRight.begin(), vecRight.end());

	int forSize = vecLeft.size();

	for (int i = 0; i < forSize; i++) {
		int counter = 0;
		int leftNum = vecLeft[i];
		for (int j = 0; j < forSize; j++) {
			if (vecLeft[i] == vecRight[j]) {
				counter++;
			}
		}
		simres += leftNum * counter;
		diffres += abs(leftNum - vecRight[i]);
	}

	cout << "Part 1: " << diffres << endl;
	cout << "Part 2: " << simres << endl;

	// Close the file
	MyReadFile.close();
}
