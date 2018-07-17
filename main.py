from flask import request, jsonify, abort, Flask
import requests, os
from tracker import *
from game import *

app = Flask(__name__)

# helper function to format the messages
def create_message(msg):
	return jsonify(
		response_type = 'in_channel',
		attachments = [{
			"text": msg,
	    "color": "#3AA3E3",
	    "attachment_type": "default"
	 }])

# validate_request function is necessary
def valid_request(request):
	is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
	is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']
	return is_token_valid and is_team_id_valid

@app.route('/command', methods=['POST', 'GET'])
def gettingResponse():
	if not valid_request(request):
		abort(400)

	# sorting out the content in the message
	command = request.form['text'].split()
	channel = request.form['channel_id']
	curr_user = request.form['user_name']

	if command[0] == "challenge":
		player_one = request.form['user_name']
		player_two = command[1][1:]
		if (can_start_game(channel)):
			start_game(channel, player_one, player_two)
			return create_message("*new game:* " + player_one + " :x: vs " + player_two +" :o: \n" + display_board(channels[channel]['board']) + "\n *Current turn:* " + channels[channel]['turn'])
		else:
			return create_message("You can't challenge " + player_two + " because a match is currently going on!")
	elif command[0] == "make_move":
		if (allowed_to_make_move(channel, curr_user)): # if move is possible...
			move = int(command[1])
			# calling the `make_move` method to see what happens
			# when user makes this particular move
			outcome = make_move(channel, move, curr_user)
			# if outcome is an empty string, game continues
			if outcome == "":
				return create_message("*ongoing game:* " + channels[channel]['players'][0] + " :x: vs " + channels[channel]['players'][1] +" :o: \n" + display_board(channels[channel]['board']) + "\n *It's turn: *" + channels[channel]['turn'])
			# different error messages for different scenario
			elif (outcome == "Please make a valid move!"):
				return create_message("Please make a valid move!\n*Ongoing game:* " + channels[channel]['players'][0] + ":x: vs " + channels[channel]['players'][1] +":o: \n" + display_board(channels[channel]['board']) + "\n *It's turn: *" + channels[channel]['turn'])
			elif (outcome == "Ops, you can't make a move right now!"):
				return create_message("Ops, you can't make a move right now!")
			else:
				# if it's none of the above, it means the game has ended
				if outcome == "Draw":
					return create_message("It's over! Game ended in a draw!")
				else:
					return create_message("It's over! "+ outcome +" won this match!")
		else:
			return create_message("Ops, you're not allowed to make a move!")
	elif command[0] == "display":
		if (channel in channels):
			if (channels[channel]["ongoing"]):
				text = "The game currently: \n" + display_board(channels[channel]['board']) + "\n It's "+ channels[channel]['turn'] +"'s to make a move!"
				return create_message(text)
		return create_message("There is currently no ongoing game!")
	elif command[0] == "turn":
		return create_message("It's " + channels[channel]["turn"] + "'s to make a move!")
	elif command[0] == "help":
		possible_commands = "Here are the possible commands you can make with this `/ttt` slash command:\n" \
			"`/ttt turn`: allows you to see which player's turn it is\n" \
			"`/ttt make_move NUMBER`: allows you to make a move on space NUMBER on the board\n" \
			"`/ttt challenge @user`: allows you to start a game with someone in your workplace\n" \
			"`/ttt display`: allows you to view the board of a game if it's ongoing"
		return create_message(possible_commands)
	else:
		return create_message("You typed in an invalid command! Do you need help? Type `/ttt help` for a list of possible commands")

if __name__ == "__main__":
	app.run('localhost', 80)