#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int search2D(vector<vector<char>>& grid, int& row, int& col, string& word) {
    int m = grid.size();
    int n = grid[0].size();

	int count = 0;
    
    if (grid[row][col] != word[0])
      return false;
 
    int len = word.size();
    
    // direction in which word needs to be searched.
    vector<int> x = { -1, -1, -1, 0, 0, 1, 1, 1 };
    vector<int> y = { -1, 0, 1, -1, 1, -1, 0, 1 };
 
    // return true if one of the directions contain the word.
    for (int dir = 0; dir < 8; dir++) {
        int k, currX = row + x[dir], currY = col + y[dir];

        for (k = 1; k < len; k++) {
            if (currX >= m || currX < 0 || currY >= n || currY < 0){
				break;
			} 
            if (grid[currX][currY] != word[k]){
				break;
			}
            currX += x[dir], currY += y[dir];
        }
        if (k == len){
			count++;
		}
    }
    return count;
}

vector<vector<int>> searchWord(vector<vector<char>>& grid, string& word){
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> ans;
    
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            int count = search2D(grid, i, j, word);
			if (count > 0){
				ans.push_back({i, j, count});
			}
        }
    }
    return ans;
}

void printResult(vector<vector<int>>& ans){
	int count = 0;
    for (int i = 0; i < ans.size(); i++) {
        cout << "{" << ans[i][0] << "," << ans[i][1] << "}" << " count: " << ans[i][2] << " ";
		count += ans[i][2];
    }
    cout << endl;
	cout << "Total count: " << count << endl;
}

int main() {
	string line;
	ifstream readFile("input.txt");
	vector<vector<char>> grid;
	string wordToFind = "XMAS";

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
