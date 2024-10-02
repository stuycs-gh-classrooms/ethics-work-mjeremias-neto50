board = [[" "," "," "],[" "," "," "],[" "," "," "]]
win = False
p1 = True
Board = ''' 1 # 2 # 3
1'''+ board[0][0] + ''' # '''  + board[0][1] + ''' # ''' + board[0][2] + '''
   #   #
###########
   #   #
2'''+board[1][0]+''' # ''' + board[1][1] + ''' # ''' + board[1][2] + '''
   #   #
###########
   #   #
3'''+board[1][0]+''' # ''' + board[1][1] + ''' # ''' + board[1][2] + '''
   #   #   '''

while (not win):
    Board = ''' 1 # 2 # 3
1'''+ board[0][0] + ''' # '''  + board[0][1] + ''' # ''' + board[0][2] + '''
   #   #
###########
   #   #
2'''+board[1][0]+''' # ''' + board[1][1] + ''' # ''' + board[1][2] + '''
   #   #
###########
   #   #
3'''+board[1][0]+''' # ''' + board[1][1] + ''' # ''' + board[1][2] + '''
   #   #   '''
    if(board[0][0] == board[0][1] and board[0][0] == board[0][2]):
       win = True
    if(board[1][0] == board[1][1] and board[1][0] == board[1][2]):
        win = True
    if(board[2][0] == board[2][1] and board[2][0] == board[2][2]):
        win = True
    if(board[0][0] == board[1][0] and board[0][0] == board[2][0]):
       win = True
    if(board[0][1] == board[1][1] and board[0][1] == board[2][1]):
        win = True
    if(board[0][2] == board[1][2] and board[0][2] == board[2][2]):
        win = True
    if(board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        win = True
    if(board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        win = True
    if win:
        break
    
    if p1:
        print(Board)
        print("")
        print("X, what row do you want to place your X?")
        row = input(" ")
        print("X, what column do you want to place your X?")
        column = input(" ")
        row = int(row)
        column = int(column)
        if(board[row-1][column-1] == " "):
            board[row - 1][column - 1] = "X"
            p1 = not p1
        else:
            print("try again, nerd")
            print("")
    else:
        print(Board)
        print("")
        print("O, what row do you want to place your O?")
        row = input(" ")
        print("O, what column do you want to place your O?")
        column = input(" ")
        row = int(row)
        column = int(column)
        if(board[row-1][column-1] == " "):
            board[row - 1][column - 1] = "O"
            p1 = not p1
        else:
            print("try again, nerd")
            print("")
if p1:
    print("O wins!!!!!!!!!")
else:
    print("X wins!!!!!!!!!")