#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector<vector<int>> search2D(vector<vector<char>>& grid, int& row, int& col, string& word) {
    int m = grid.size();
    int n = grid[0].size();
    
    vector<vector<int>> matches;
    if (grid[row][col] != word[0])
      return matches;
 
    int len = word.size();
    
    // direction in which word needs to be searched.
    vector<int> x = { -1, -1, 1, 1 };
    vector<int> y = { -1, 1, -1, 1 };
 
    // return true if one of the directions contain the word.
    for (int dir = 0; dir < 4; dir++) {
        vector<int> match = {row, col};

        int k, currX = row + x[dir], currY = col + y[dir];

        for (k = 1; k < len; k++) {
            if (currX >= m || currX < 0 || currY >= n || currY < 0){
				break;
			}
            if (grid[currX][currY] != word[k]){
				break;
			}
            match.push_back(currX);
            match.push_back(currY);
            currX += x[dir], currY += y[dir];
        }
        if (k == len){
			matches.push_back(match);
		}
    }
    return matches;
}

vector<vector<int>> searchWord(vector<vector<char>>& grid, string& word){
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> matches;
    
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            vector<vector<int>> returnmatches = search2D(grid, i, j, word);
            matches.insert(matches.end(), returnmatches.begin(), returnmatches.end());
        }
    }
    return matches;
}

void printResult(vector<vector<int>>& ans){
    vector<vector<int>> middleLetters;
    vector<vector<int>> checkDuplicates;
    for (int i = 0; i < ans.size(); i++) {
        vector<int> middle = { ans[i][2], ans[i][3] };
        middleLetters.push_back(middle);
    }
    int count = 0;
    for (vector<int> vec : middleLetters){
        auto it = find(checkDuplicates.begin(), checkDuplicates.end(), vec);
        if ( it != checkDuplicates.end() ){
            count++;
        }
        checkDuplicates.push_back(vec);
        cout << "{" << vec[0] << "," << vec[1] << "}" << endl;
    }
    cout << endl;
    cout << count;
}

int main() {
	string line;
	ifstream readFile("input.txt");
	vector<vector<char>> grid;
	string wordToFind = "MAS";

	// Parse to 2D grid
	while (getline(readFile, line)) {
		vector<char> lineVec;
		for(char& c : line ) {
			lineVec.push_back(c);
		}
		grid.push_back(lineVec);
	}

	for(vector<char> row : grid){
		for(char c : row){
			cout << c;
		}
		cout << endl;
	}

	vector<vector<int>> ans = searchWord(grid, wordToFind);
    
    printResult(ans);

	readFile.close();
}
