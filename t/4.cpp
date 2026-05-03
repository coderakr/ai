#include <iostream>
using namespace std;

#define N 4  // Change N for different board sizes

// Function to print the solution
void printSolution(int board[N][N]) {
    cout << "Solution:\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Check if it's safe to place queen at board[row][col]
bool isSafe(int board[N][N], int row, int col) {

    // Check column
    for (int i = 0; i < row; i++) {
        if (board[i][col])
            return false;
    }

    // Check left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j])
            return false;
    }

    // Check right diagonal
    for (int i = row, j = col; i >= 0 && j < N; i--, j++) {
        if (board[i][j])
            return false;
    }

    return true;
}

// Backtracking function
bool solveNQ(int board[N][N], int row) {

    // If all queens are placed
    if (row == N)
        return true;

    // Try placing queen in all columns
    for (int col = 0; col < N; col++) {

        if (isSafe(board, row, col)) {

            // Place queen
            board[row][col] = 1;

            // Recur for next row
            if (solveNQ(board, row + 1))
                return true;

            // Backtrack
            board[row][col] = 0;
        }
    }

    return false;
}

// Main function
int main() {
    int board[N][N] = {0};

    if (solveNQ(board, 0)) {
        printSolution(board);
    } else {
        cout << "No solution exists";
    }

    return 0;
}