class TicTacToe:
	def __init__(self):
		self.board = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
		self.player_one = ""	# X
		self.player_two = ""	# O
		self.turn = ""
		self.ongoing = False
		self.winning_combos = {0: [[0, 2], [3, 6], [4, 8]],
								1: [[0, 2], [4, 7]],
								2: [[0, 1], [5, 8]],
								3: [[4, 5], [0, 6]],
								4: [[0, 8], [2, 6], [1, 7], [3, 5]],
								5: [[2, 8], [3, 4]],
								6: [[0, 3],[7, 8], [2, 4]],
								7: [[6, 8], [1, 4]],
								8: [[6, 7], [2, 5], [0, 4]]}
		self.winner = ""

	def reset(self):
		self.board = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
		self.player_one = ""	# X
		self.player_two = ""	# O
		self.turn = ""
		self.ongoing = True

	def set_turn(self, player):
		self.turn = player

	def display_board(self):
		return(self.board[0]+"|" + self.board[1]+ "|" +self.board[2]+
				"\n–––––––––\n" +
				self.board[3]+"|" + self.board[4]+ "|" +self.board[5] +
				"\n–––––––––\n" +
				self.board[6]+"|" + self.board[7]+ "|" +self.board[8])

	def is_board_full(self):
		choices = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
		for i in range(len(self.board)):
			if self.board[i] in choices:
				return False
		return True

	def switch_turns(self, player):
		if (self.player_one == player):
			self.turn = self.player_two
		else:
			self.turn = self.player_one

	def check_valid_move(self, move):
		return(self.board[move] != ":x:" or self.board[move] != ":o:") # valid move, not empty

	def correct_turn(self, player):
		return(player==self.turn)

	def check(self, place):
		# if someone wins, their symbol will be returned
		# else, if the game is still ongoing, an empty string will be returned
		rows_to_check = self.winning_combos[place]
		for row in rows_to_check:
			if (self.board[row[0]]==self.board[row[1]]==self.board[place]==":x:"):
				self.winner = self.player_one
				self.ongoing = False
				return(self.winner)
			elif (self.board[row[0]]==self.board[row[1]]==self.board[place]==":o:"):
				self.winner = self.player_two
				self.ongoing = False
				return(self.winner)
		if (self.is_board_full()): # if the board is full, it's a tie
			self.winner = "Draw"
			self.ongoing = False
			return(self.winner)
		return("")

	def make_move(self, place, player):
		if (self.correct_turn(player)):
			if (self.check_valid_move(place)):
				if (player == self.player_one):
					self.board[place] = ":x:"
					self.turn = self.player_two
				else:
					self.board[place] = ":o:"
					self.turn = self.player_one
			else:
				return("Please make a valid move!")
		else:
			return("Ops, you can't make a move right now!")
		return(self.check(place)) # returns whether the game is finished or not
