Consider the game sudoku.
Using the provided file, sudoku.py, as a starting point, we are going to 
be implementing the AC3 algorithm for sudoku.

Several helper functions functions, are implemented to help you start. One simply prints out a sudoku board, the other checks if the sudoku board is solved. A main function with 3 example problems is also written.

Implement the function solve_sudoku, which takes in a sudoku board as a 2d list of size [9][9]. Blank spots are represented as '*', all other spots have digits places. The function does not need a return value, as python list passing is by reference.

Submit your code and a README in a zip file.

Do not wait until the last minute to start this!
We will go over the starter code in class.

My solution consists of a Variable Class, which contains the position of the variable relative to the board, it's domain [1-9], and the board.
Within the class, contains a method that makes sure the variable is arc consistent by calling other helper methods. Once this method is done, the domain
of the variable changes.

My solution creates Variables for all positions that are empty in the Suduko board and stored in a q. While the q is not empty then q pops a variable 
and calls the variable's method to make it arc consistent. If the variable's domain only contains 1 number, then that number is filled in the sudoku 
board for the variable's position. Else the Variable is appended to the q again. This is repeatedly done to all variables, until the q is empty, which 
would signify that the board has been solved.

