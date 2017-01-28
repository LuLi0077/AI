# Diagonal Sudoku Solver

Writing an AI agent to solve every diagonal sudoku puzzle. A diagonal sudoku is like a regular sudoku, except that among the two main diagonals, the numbers 1 to 9 should all appear exactly once. The approach is inspired by Peter Norvig's essay on [Solving Every Sudoku Puzzle](http://norvig.com/sudoku.html). 


### Code

* `Sudoku.ipynb` - notebook version of solution code, includes testing process and lecture notes 
* `solutions.py` - solution code
* `solution_test.py` - test solution by running `python solution_test.py`
* `PySudoku.py` -  code for visualizing the solution
* `visualize.py` - code for visualizing the solution


### Question 1 (Naked Twins)

Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked twins problem states if there are two unsolved boxes in a unit and there are two digits that can only go in the same two boxes, then no others peers in that unit can have the two digits. The approach is:
1. Use "elimination" where if a box has a value assigned, then none of the peers of this box can have this value.
2. Search within each unit to see if there are any "twins" which are the two same digits in two boxes
3. If there are twins, and it's possible there are multiple twins within a unit, then for each pair of twins - search each box within the unit where it contains the value of the digits in the twins and remove them. 


### Question 2 (Diagonal Sudoku)

Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: This just requires one addition to the regular sudoku solution - adding the two diagonal units to the unitlist and serve as constraints while performing reduce and search functions.  
