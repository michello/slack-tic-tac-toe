# container to store data about ongoing games
# format:
'''
 channels : {
	channel_id: {
		'ongoing': BOOLEAN,
		'players': ARRAY,
		'winner': STRING,
		'turn': players[0], // initializing to the first player
		'board': [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
	}
}
'''
channels = {}

# function to see if a game is ongoing or not
def can_start_game(channel):
	if channel in channels:
		# can't start a game if there is one already ongoing in this channel
		if (channels[channel]['ongoing']):
			return(False)
	else:
		# if it's the first time a game is getting created in a channel,
		# initialize an empty dict
		channels[channel] = {}
	return(True)

def start_game(channel, player_one, player_two):
	# initializing channel variables when starting the game
	channels[channel]['ongoing'] = True
	channels[channel]['players'] = []
	channels[channel]['players'].append(player_one)
	channels[channel]['players'].append(player_two)
	channels[channel]['winner'] = ""
	channels[channel]['turn'] = player_one
	channels[channel]['board'] = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]

def allowed_to_make_move(channel, player):
	# makes sure the user is one of the players in this particular game
	# AND it's the user's turn to make a move
	return (player in channels[channel]['players'] and channels[channel]['turn'] == player)