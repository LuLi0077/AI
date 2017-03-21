# Constraint Satisfaction

Constraint Satisfaction is a technique for solving problems by expressing limits on the values of each variable in the solution with mathematical constraints.  We've used constraints before -- constraints in the Sudoku project are enforced implicitly by filtering the legal values for each box, and the planning project represents constraints as arcs connecting nodes in the planning graph -- but in this lab exercise we will use a symbolic math library to explicitly construct binary constraints and then use Backtracking to solve the N-queens problem (which is a generalization [8-queens problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle)).  Using symbolic constraints should make it easier to visualize and reason about the constraints (especially for debugging), but comes with a performance penalty.

![8-queens puzzle solution](EightQueens.gif)

Briefly, the 8-queens problem asks you to place 8 queens on a standard 8x8 chessboard such that none of the queens are in "check" (i.e., no two queens occupy the same row, column, or diagonal). The N-queens problem generalizes the puzzle to to any size square board.

### Main Steps
1. Overview
2. Representing the N-Queens Problem
3. Backtracking Search