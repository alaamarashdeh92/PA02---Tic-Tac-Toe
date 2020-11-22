# Tic-Tac-Toe

#
# Global variables
#

# TODO: Define your global variables here

# Game loop
is_running = False

# Players
players = None
player1 = 'X'
player2 = 'O'
player_turn = 1



# Game board
board = [''] * 10

def initalize_game():
    # TODO: Initialize your game board. Hint: All spaces should have '#'
    print("\n")
    print(f"\t{'#'}\t|\t{'#'}\t|\t{'#'}")
    print(f"\t{'#'}\t|\t{'#'}\t|\t{'#'}")
    print(f"\t{'#'}\t|\t{'#'}\t|\t{'#'}")
    print("\n")
   
    # TODO: Assign players by calling your assign_players() function
    assign_players()


    # TODO: Initialize player turn to player 1
    player_turn = player1

def display_board(board):
    
    # TODO: Print the game board
    print("\n")
    print(f"\t{board[6]}\t|\t{board[7]}\t|\t{board[8]}")
    print(f"\t{board[3]}\t|\t{board[4]}\t|\t{board[5]}")
    print(f"\t{board[0]}\t|\t{board[1]}\t|\t{board[2]}")
    print("\n")

    print(board)


def place_marker(board, player, position):
#     # TODO: Place the player marker on the board at position and return the board
    if board[position] == 0:
        board[position] = player
        return board

    display_board(board)
    

    


def check_space(board, position):
    # TODO: Check if position on the board is empty
    if position in range (len(board)):
        return True
    else:
        # print("Invalid position. Try again.")
        return False
    print("Invalid position. Try again.")



def player_choice(player, board):
    
    # TODO: Ask the player to choose a space on the board,
    player = int(input("\n Please choose a space on the board: "))
    # Check if the player choice is valid (between 0-8)
    for player in range (len(board)):
        player_turn = player1
    else:
        player_turn = player2

    # Check if the player choice is empty
    check_space(board, range(len(board)))


def assign_players():
    player1 = input("\n Please pick a marker 'X' or 'O': ")
    while True:
        # TODO: Check if player1 chose 'X', then set player2 to 'O' and return the players 
        if player1 == 'X':
            return player1 
        elif player2 == 'O':
            return player2 
        else:
            print (" invalid enter")
        # Do not forget to check the other cases.



def check_board_full(board):
    # TODO: Check if the board is full by counting the number of spaces left.
    
    return len([x for x in board if x == '#']) == 1
        

def check_win(board, mark):
     if (board.count(player1) + board.count(player2)) > 4:
        # TODO: Check rows for a win
        if (board[0] and board[1] and board[2]) == mark or (board[3] and board[4] and board[5]) == mark or (board[6] and board[7] and board[8]) == mark:
            return True
    # TODO: Check coloumns for a win
        elif (board[0] and board[3] and board[6]) == mark or (board[1] and board[4] and board[7]) == mark or (board[2] and board[5] and board[8]) == mark:
            return True
    # TODO: Check diagonals for a win
        elif (board[0] and board[4] and board[8]) == mark or (board[2] and board[4] and board[6]) == mark:
            return True
        else:
            return False
    
 

def replay():
    # TODO: Ask if the player wishes to start a new game
    print("Do you want to play agaun y / n")
    if 'y':
        return True
    else:
        return False

# DO NOT CHANGE THE LINE BELOW

if __name__ == "__main__":
    print('\n Welcome to Tic-Tac-Toe!')
    
    # TODO: Call you initialize_game() function
    is_running = True

    initalize_game()

    while is_running:
        
        
        # TODO: Check if the board is full
        check_board_full(board)
        
        # TODO While the board is not full
        
        # TODO: Check if the player_turn value is odd or even, and set marker to the correct player
        global current_player
        if player_turn % 2 == 0 :
            current_player = player2
        else:
            current_player = player1  
        # TODO: Call your player_choice() function to ask the user for a position
        player_choice(player1, board)
        # TODO: Call your place_marker() function to place the marker on the board
        place_marker(board, player1, 5)
       
        # TODO: Display the board
        
        # TODO: Increment the player turn counter

        # TODO: Check if there is a winner on the board
        check_win(board, 'X')
        # TODO: Check if the user wishes to play again
        replay()