My solution consists of a Variable Class, which contains the position of the variable relative to the board, it's domain [1-9], and the board.
Within the class, contains a method that makes sure the variable is arc consistent by calling other helper methods. Once this method is done, the domain
of the variable changes.

My solution creates Variables for all positions that are empty in the Suduko board and stored in a q. While the q is not empty then q pops a variable 
and calls the variable's method to make it arc consistent. If the variable's domain only contains 1 number, then that number is filled in the sudoku 
board for the variable's position. Else the Variable is appended to the q again. This is repeatedly done to all variables, until the q is empty, which 
would signify that the board has been solved.

