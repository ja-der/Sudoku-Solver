board = [
    [0,9,1,2,0,0,8,3,0],
    [0,0,0,0,0,6,0,0,0],
    [0,2,0,0,0,9,0,4,7],
    [0,5,0,0,0,3,0,8,0],
    [6,0,0,4,1,0,0,0,0],
    [1,0,0,8,0,0,0,9,5],
    [0,6,0,9,0,0,0,2,0],
    [0,0,2,3,0,0,0,0,4],
    [8,3,0,0,4,0,1,6,0],
]

# Will print board for dev purposes
def print_puzzle(board):
    for i in range(len(board)):
        if (i % 3 == 0 and i != 0):
            print("- - - - - - - - - - - -")
            
        for j in range (len(board[0])):
            if (j % 3 == 0 and j != 0):
                print("| ", end = "")
            
            if (j == 8):
                print(board[i][j])

            else:
                print(str(board[i][j]), end ="  ")


# Will look for cells that need to be filled in (in the case, the cells filled with 0s)
def find_missing(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == 0):
                return (i , j)
    
    return None

def check (board, num, position):

    # Check if possibility is valid in its column
    for j in range(len(board)):
        if (board[j][position[1]] == num and position[0] != j):
            return False;

    # Check if possibility is valid in its row
    for i in range(len(board[0])):
        if (board[position[0]][i] == num and position[1] != i):
            return False

    # Identifies which box the missing position is in
    x = (position[1] // 3) * 3
    y = (position[0] // 3) * 3

    # Check if possibility is valid in its box
    for i in range(y, y + 3):
        for j in range(x, x +3):
            if (board[i][j] == num and i != position[0] and j != position[1]):
                return False
    
    return True

def find_solution(board):

    pos_empty = find_missing(board)

    if pos_empty is None:
        return True
    else:
        row, col = pos_empty

        for i in range(1, 10):
            if (check(board, i, (row, col))):
                board[row][col] = i

                if (find_solution(board)):
                    return True

                board[row][col] = 0
                
        return False

print_puzzle(board)
find_solution(board)
print("Solved")
print_puzzle(board)
