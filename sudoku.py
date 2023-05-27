# Takes in 2D List representing the board and outputs it to the console as a sudoku board
def print_sudoku(board):
    if len(board) != 9:
        print("ERROR, Invalid board passed to print_sudoku")
    for row in range(9):
        if len(board[row]) != 9:
            print("ERROR, Invalid board passed to print_sudoku")
        if row % 3 == 0 and row != 0:
            print("---------------------")
        line = ""
        for col in range(9):
            if col % 3 == 0 and col != 0:
                line = line + "| "
            if board[row][col] is None:
                line = line + "* "
            else:
                line = line + str(board[row][col]) + " "
        print(line)


# Takes in 2D List representing the board and returns True if the problem is solved in a valid way
def check_sudoku(board):
    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Check there are no empty cells
    for row in board:
        for col in row:
            if col not in domain:
                return False

    # Check rows for AllDiff
    for row in board:
        if len(row) != len(set(row)):
            return False

    # Check cols for AllDiff
    for i in range(9):
        col = [row[i] for row  in board]
        if len(col) != len(set(col)):
            return False

    # Check subsquare for AllDiff
    for i in range(3):
        for j in range(3):
            subsquare = [board[3*i][3*j],     board[3*i][3*j + 1],     board[3*i][3*j + 2],
                         board[3*i + 1][3*j], board[3*i + 1][3*j + 1], board[3*i + 1][3*j + 2],
                         board[3*i + 2][3*j], board[3*i + 2][3*j + 1], board[3*i + 2][3*j + 2]]
            if len(subsquare) != len(set(subsquare)):
                return False
    return True

# START OF MY SOLUTION--------------------------------------------------------------------
class Variable:
    def __init__(self, pos, board=None):
        self.pos = pos
        self.board = board
        self.domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def arcConsistent(self):
        # if self.board[self.pos[0]][self.pos[1]] != None: 
        #     self.domain = {self.board[self.pos[0]][self.pos[1]]}
        #     return
        self.__columnConstraints()
        self.__rowConstraints()
        self.__subSquareConstraints()
    def __columnConstraints(self):
        for row in range(9):
            if self.board[row][self.pos[1]] == None or row == self.pos[0]: continue

            try:
                self.domain.remove(self.board[row][self.pos[1]])
            except:
                continue
    def __rowConstraints(self):
        for col in range(9):
            if self.board[self.pos[0]][col] == None or col == self.pos[1]: continue
            
            try:
                self.domain.remove(self.board[self.pos[0]][col])
            except:
                continue
    def __subSquareConstraints(self):
        row, col = self.__findSubSquareOf(self.pos[0], self.pos[1])
        i, j = (0,0)

        for x in range(9):
            if x==3 or x==6: i+=1
            if j == 3: j = 0
            if row+i == self.pos[0] and col+j == self.pos[1]: continue
            try:
                self.domain.remove(self.board[row+i][col+j])
            except:
                pass

            j+=1
    def __findSubSquareOf(self, row, col):
        # find subSquare pos belongs to
        # starting index of subsquares:
            # (0,0), (0, 3), (0,6)
            # (3,0), (3, 3), (3,6)
            # (6,0), (6, 3), (6,6)

        if row < 3 and col < 3: return (0,0)
        if row < 3 and col < 6: return (0,3)
        if row < 3 and col < 9: return (0,6)

        if row < 6 and col < 3: return (3,0)
        if row < 6 and col < 6: return (3,3)
        if row < 6 and col < 9: return (3,6)
        
        if row < 9 and col < 3: return (6,0)
        if row < 9 and col < 6: return (6,3)
        if row < 9 and col < 9: return (6,6)

    def numOfOptions(self):
        return len(self.domain)

def solve_sudoku(board):
    arcs = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == None: arcs.append(Variable((row,col))) 

    while len(arcs) != 0:
        arc = arcs.pop(0)
        arc.board = board
        arc.arcConsistent()
        
        if arc.numOfOptions() == 1:
            board[arc.pos[0]][arc.pos[1]] = arc.domain.pop()
        else:
            arcs.append(arc) 
# END OF SOLUTION-------------------------------------------------------


problem1 = [[None, None, 3   ,      None, 2   , None,       6   , None, None],
            [9   , None, None,      3   , None, 5   ,       None, None, 1   ],
            [None, None, 1   ,      8   , None, 6   ,       4   , None, None],

            [None, None, 8   ,      1   , None, 2   ,       9   , None, None],
            [7   , None, None,      None, None, None,       None, None, 8   ],
            [None, None, 6   ,      7   , None, 8   ,       2   , None, None],

            [None, None, 2   ,      6   , None, 9   ,       5   , None, None],
            [8   , None, None,      2   , None, 3   ,       None, None, 9   ],
            [None, None, 5   ,      None, 1   , None,       3   , None, None]]

problem2 = [[None, 1   , 3   , 4   , 2   , None, None, 8   , 6   ],
            [2   , None, 4   , 6   , None, None, None, None, None],
            [None, 8   , 7   , None, 1   , None, 3   , None, None],
            [None, None, None, None, 3   , None, 6   , None, None],
            [None, 6   , 2   , 5   , None, None, None, None, 3   ],
            [5   , None, None, 7   , 6   , 4   , None, 9   , 1   ],
            [7   , None, None, None, 4   , None, 8   , 1   , None],
            [None, 4   , None, 8   , None, None, None, 6   , None],
            [None, None, 1   , 2   , 5   , 6   , None, 3   , 7   ]]

problem3 = [[6   , None, None, None, None, 7   , None, 2   , None],
            [None, None, None, None, None, None, None, 1   , 5   ],
            [2   , 4   , 9   , None, 1   , None, None, None, 3   ],
            [4   , None, 5   , 8   , None, 1   , 3   , 9   , None],
            [3   , 8   , None, None, 4   , 9   , None, None, None],
            [None, 1   , 6   , None, 7   , None, None, None, None],
            [8   , None, 4   , 1   , 5   , 3   , 6   , None, 2   ],
            [None, None, None, None, 6   , 4   , 8   , 3   , None],
            [1   , 6   , None, None, None, 2   , None, None, 9   ]]

print('-' * 80)
print("Example 1")
print("Initial State")
print_sudoku(problem1)
solve_sudoku(problem1)
print("\nSolved: " + str(check_sudoku(problem1)))
print("Final State")
print_sudoku(problem1)
print("")

print('-' * 80)
print("Example 2")
print("Initial State")
print_sudoku(problem2)
solve_sudoku(problem2)
print("\nSolved: " + str(check_sudoku(problem2)))
print("Final State")
print_sudoku(problem2)
print("")

print('-' * 80)
print("Example 3")
print("Initial State")
print_sudoku(problem3)
solve_sudoku(problem3)
print("\nSolved: " + str(check_sudoku(problem3)))
print("Final State")
print_sudoku(problem3)
print("")
