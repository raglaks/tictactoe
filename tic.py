"""
requirements:
the program must have a user interface
the program must print the board every turn
the program must detect when either player wins
the program must ask players if they would like to play again

considerations:
there can only be a maximum of nine turns (3 * 3)
what's the best way for players to interact with the game? in other words how can player A specify that they want to place a cross in the top-right square?
how will the program detect a win/draw?

possible solutions:
limit input to 0 or 1; 0 = "o" 1 = "x"
possible list of positions?
[tl, tm, tr, ml, mm, mr, bl, bm, br]
this list can be modified as users pick so that options remaining will reflect the accurate game state

so input could be a combination of these two inputs?

pseudocode:
1. welcome screen which prompts both players for their names
2. once names have been entered, launch game and show board
3. player order should be randomized and first player should be prompted
4. once player one inputs, the board should accurately reflect the turn and player two's turn should start
5. at the end of the third turn, a win condition must trigger immediately and should do so in all following turns
6. if the win condition hasn't triggered at the end of the game, declare a draw
7. when the win is won/drawn, launch a replay function that asks if players want to play again
8. change order of players for the replay game
"""

#this function shows the welcome screen, prompts both player for their names and then should launch the game
def welcome():
  print('Welcome to tic tac toe\n')
  player1 = input('Input player one\'s name: ')
  player2 = input('\nInput player two\'s name: ')
  print(f'\n{player1}, {player2}, the game will start now...\n')

  tictactoe(player1, player2)

def replay(player1,player2):

  #switch up player orders for new game
  newp1 = player2
  newp2 = player1
  play_again = input('Type "y" if you would like to play again: ')

  #this skip var is to skip showing the players the instructions again
  skip = True

  if play_again == 'y':
    tictactoe(newp1, newp2,skip)
  else:
    print('\nHave a nice day.')

#this is where the main game takes place
def tictactoe(player1='p1',player2='p2',skip=False):

  #this string shows the instructions
  instructions = 'Player 1 will play "X" and player 2 will play "O." You will be prompted to type the position where you would like to play your move.\nTop left = TL\nTop middle = TM\nTop right = TR\nMiddle left = ML\nMiddle middle = MM\nMiddle right = MR\nBottom left = BL\nBottom middle = BM\nBottom right = BR\n' 

  #ternary that shows instructions depending on the skip var--default is false, it changes to true in the replay func
  print(instructions) if skip == False else print('\nThe player order has been switched, good luck.\n')

  #the main while loop is based on this variable (there can only be nine turns max in any given game)
  turns = 9

  #this dictionary houses all the possible board positions and updates if the position is played
  #the default value is an underscore because it will print it to the board to simulate blank positions
  pos_dict = {'TL': '_', 'TM': '_', 'TR': '_', 'ML': '_', 'MM': '_', 'MR': '_', 'BL': '_', 'BM': '_', 'BR': '_'}

  #win conditions
  wins = [
    ['TL', 'TM', 'TR'],
    ['ML', 'MM', 'MR'],
    ['BL', 'BM', 'BR'],
    ['TL', 'ML', 'BL'],
    ['TM', 'MM', 'BM'],
    ['TR', 'MR', 'BR'],
    ['TL', 'MM', 'BR'],
    ['TR', 'MM', 'BL'],
  ]

  #default setting for game won var
  game_won = False

  #the entire game will run while there are less than the max no. of turns (9)
  while 1 <= turns:

    #this list is updated in each iteration to show available positions on the board
    available_positions = []

    #this is the logic for the available_positions list--it sorts through the pos_dict keys, checks for positions that are still blank and appends them to the available_positions list
    for key in pos_dict.keys():
      if pos_dict[key] == "_":
        available_positions.append(key)

    #this variable is needed to show the name of the current player (to play)--it's based on the turns variable--if turns is odd, it's p1's turn and if not it's p2's turn
    current_player = player1 if turns % 2 != 0 else player2
    turn = 'X' if turns % 2 != 0 else 'O'

    #this input variable saves what position the player chooses
    position = input(f'{current_player}, please choose your position: \n{available_positions}: \n')

    #basic error handling to check for a valid position input and to also check if the position is not already filled
    if position not in pos_dict:
      print("\nPlease input a valid position\n")
      continue

    if pos_dict[position] != "_":
      print("\nThat position has already been filled, please choose another position\n")
      continue

    #the key value pair is updated to show what was played in which position
    pos_dict[position] = f"{turn}"

    #the board variable is updated and printed to reflect the last play--info is pulled from pos_dict
    board = f" |_{pos_dict['TL']}_|_{pos_dict['TM']}_|_{pos_dict['TR']}_|\n |_{pos_dict['ML']}_|_{pos_dict['MM']}_|_{pos_dict['MR']}_|\n |_{pos_dict['BL']}_|_{pos_dict['BM']}_|_{pos_dict['BR']}_|\n"

    print(board)

    #on the third turn, launch win condition checker
    if turns <= 7:

      #these empty lists are created for easier sorting of all positions with X and O values
      x = []
      o = []
      
      #this is where the sorting happens
      for key, value in pos_dict.items():
        if value == "X":
          x.append(key)
        elif value == "O":
          o.append(key)
      
      #this is where the win conditions are checked 
      #the first conditional will trigger only if there are at least three values in the x/o list
      if len(x) >= 3:
        #this loop loops through the wins list to go through each win
        for win in wins:
          #an empty list is created here for sorting purposes
          xwin = []
          #if one of the x array elements matches one of the win condition list elements, it will be pushed to xwin
          for i in x:
            if i in win:
              xwin.append(i) 
          
          #this last conditional will only check if the length of xwin == 3, because you need a combination of three positions to win
          #it also checks for an exact match of the xwin elements and the winning combo elements
          if len(xwin) == 3 and xwin[0] in win and xwin[1] in win and xwin[2] in win:
            game_won = True

      #lastly if the game_won var was triggered, the while loop will exit here, print who won and call the replay func
      if game_won:
        print(f'{current_player} won!\n')
        replay(player1, player2)
        break
            
      #exact same code but for the o list--maybe this can be refactored
      if len(o) >= 3:
        for win in wins:
          owin = []
          for i in o:
            if i in win:
              owin.append(i)
          
          if len(owin) == 3 and owin[0] in win and owin[1] in win and owin[2] in win:
            game_won = True
      
      if game_won:
        print(f'{current_player} won!\n')
        replay(player1, player2)
        break
        
    #necessary decrease of turns count for proper while loop function
    turns -= 1

  #this else statement is only launched if the while loop runs without breaks--if no one won--meaning that the game was a draw
  else:
    print('This is a drawn game.\n')
    replay(player1, player2)

#program is launched here
welcome()

