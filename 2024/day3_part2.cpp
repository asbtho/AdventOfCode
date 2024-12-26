#include <iostream>
#include <fstream>
#include <string>
#include <regex>
using namespace std;

int main() {
	// Create a text string, which is used to output the text file
	string myText;

	// Read from the text file
	ifstream MyReadFile("input.txt");

    int result = 0;
    bool dont = false;

	// Parse lines
	while (getline(MyReadFile, myText)) {
		cout << myText << endl;
        string Input = myText;
        regex Pattern{"(mul)(\\()(\\d{1,3})(,)(\\d{1,3})(\\))|(don't)(\\(\\))|(do)(\\(\\))"};
        sregex_iterator Iterator{Input.begin(), Input.end(), Pattern };
        sregex_iterator End;
        while (Iterator != End) {
            smatch results = *Iterator;
            if (results[0] == "don't()"){
                dont = true;
            } else if (results[0] == "do()"){
                dont = false;
            } else {
                if (!dont){
                    result += stoi(results[3]) * stoi(results[5]);
                    cout << results[3] << " * ";
                    cout << results[5] << endl;
                }
            }
            ++Iterator;
        }
	}

	// Close the file
	MyReadFile.close();

    cout << "Part 2: " << result << endl;
}
