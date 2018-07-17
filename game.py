from tracker import *

# a dictionary of the combos 
winning_combos = {0: [[1, 2], [3, 6], [4, 8]],
	1: [[0, 2], [4, 7]],
	2: [[0, 1], [5, 8]],
	3: [[4, 5], [0, 6]],
	4: [[0, 8], [2, 6], [1, 7], [3, 5]],
	5: [[2, 8], [3, 4]],
	6: [[0, 3],[7, 8], [2, 4]],
	7: [[6, 8], [1, 4]],
	8: [[6, 7], [2, 5], [0, 4]]}

# function to display the board properly
def display_board(board):
	return(board[0]+"|" + board[1] + "|" + board[2] +
		"\n–––––––––\n" +
		board[3] +"|" + board[4] + "|" + board[5] +
		"\n–––––––––\n" +
		board[6]+"|" + board[7] + "|" + board[8])

# checks if the board is full
def is_board_full(board):
	choices = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
	for i in range(len(board)):
		if board[i] in choices:
			return False
	return True

# checks if the space the player picks is available to make or not
def check_valid_move(channel, move):
	return(channels[channel]['board'][move] != ":x:" and channels[channel]['board'][move] != ":o:") # valid move, not empty

# checks for what the outcome will be after a player has made a move
def check_for_final_outcome(place, channel):
	board = channels[channel]['board']
	rows_to_check = winning_combos[place]
	# iterating through the combos to check if a combo has been fulfilled
	# if it has, that means the player is a winner
	for row in rows_to_check: 
		if (board[row[0]]==board[row[1]]==board[place]==":x:"):
			channels[channel]['winner'] = channels[channel]['players'][0]
			channels[channel]['ongoing'] = False
			return(channels[channel]['winner'])
		elif (board[row[0]]==board[row[1]]==board[place]==":o:"):
			channels[channel]['winner'] = channels[channel]['players'][1]
			channels[channel]['ongoing'] = False
			return(channels[channel]['winner'])
	# if not, then we check if the board is full for a draw
	if (is_board_full(board)): 
		channels[channel]['winner'] = "Draw"
		channels[channel]['ongoing'] = False
		return(channels[channel]['winner'])
	# the game continues if the board isn't full and if there is no winner
	return("")

def make_move(channel, place, player):
	place -= 1
	# checks if the place the player specifies is valid or not
	if (check_valid_move(channel, place)):
		# if the place is valid, we're now checking which player this is
		# so we can record the appropriate value in our board tracker 
		# and switch the turn to the other player
		if (player == channels[channel]['players'][0]):
			channels[channel]['board'][place] = ":x:"
			channels[channel]['turn'] = channels[channel]['players'][1]
		else:
			channels[channel]['board'][place] = ":o:"
			channels[channel]['turn'] = channels[channel]['players'][0]
	else:
		# if the place the player specifies is not valid,
		# we return an error message
		return("Please make a valid move!")
	# after the player makes a move, we check whether this move results
	# in a win, a draw or nothing (which would continue the game).
	return(check_for_final_outcome(place, channel))