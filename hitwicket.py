# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-","-","-",
         "-", "-", "-","-","-",
         "-", "-", "-","-","-",
         "-", "-", "-","-","-",
         "-", "-", "-","-","-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None
playerX_life=5
player0_life=5
# Tells us who the current player is (X goes first)
current_player = "X"
next_player="0"
# Play the game
def play_game():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + " | " +board[3] +" | "+board[4] + "          1 | 2 | 3 | 4 | 5 ")
  print(board[5] + " | " + board[6] + " | " + board[7] +" | " +board[8] +" | " + board[9] +"          6 | 7 | 8 | 9 | 10 ")
  print(board[10] + " | " + board[11] + " | " + board[12] +" | " +board[13] +" | " + board[14] + "          11|12 |13| 14| 15")
  print(board[15] + " | " + board[16] +" | " + board[17]+" | " +board[18]+" | " + board[19] + "          16 |17|18 |19 | 20")
  print(board[20] + " | " + board[21] + " | " + board[22] +" | " +board[23]+" | " + board[24] + "          21 |22 |23 |24 |25")
  print("\n")



def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-25: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while int(position) not in range(1,26):                #["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-" or board[position] != player:
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()

def flip_player():
  # Global variables we need
  global current_player,next_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
    next_player="X"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"
    next_player = "0"
# Check if the game is over
def check_if_game_over():
  check_for_winner()

def check_for_attack(player,position,otherplayerlife):
    if(board[position+1]==next_player or board[position-1]==next_player or board[position+5]==next_player or board[position-5]==next_player ):
        otherplayerlife-=1

def check_if_game_over():
  check_for_winner()
def check_for_winner():
    global winner
    if(playerX_life==0) : winner="0"
    if(player0_life==0) :winner="X"


play_game()