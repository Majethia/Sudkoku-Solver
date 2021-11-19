input_board = '100904082052680300864200910010049806498300701607010093086035209509002130030497008'

def convert_input(input_from_window):
    c = list(input_from_window)
    d = []
    for i in range(81):
        e = int(c[i])
        d.append(e)

    e = [d[0:9], d[9:18], d[18:27], d[27:36], d[36:45], d[45:54], d[54:63], d[63:72], d[72:81]]
    return e

def result_board(bo):
    a = ''
    for i in range(9):
        if i % 3 == 0 and i != 0:
            a = a + '- - - - - - - - - - -\n'

        for j in range(9):
            if j % 3 == 0 and j != 0:
                a = a + '| '
            
            if j == 8:
                a = a + str(bo[i][j]) + '\n'
            else:
                a = a + str(bo[i][j]) + ' '
    return a

def valid(bo, num, pos):
    # check rows
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    # check columns
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check Blocks
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 2):
        for j in range(box_x * 3, box_x*3 + 2):
            if bo[i][j] == num and pos != (i,j):
                return False
    return True

def check_input_validity(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                pass
            elif valid(bo, bo[i][j], (i,j)):
                pass
            else:
                return False
    return True

board = convert_input(input_board)
print(check_input_validity(board))