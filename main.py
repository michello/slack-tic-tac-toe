from flask import request, jsonify, abort, Flask
import game
import requests, os
# import history

app = Flask(__name__)

aGame = game.TicTacToe()

def valid_request(request):
	is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
	is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']
	return is_token_valid and is_team_id_valid

@app.route('/command', methods=['POST', 'GET'])
def gettingResponse():
	if not valid_request(request):
		abort(400)

	command = request.form['text'].split()

	if command[0] == "challenge":
		# aGame = game.TicTacToe()
		if not aGame.ongoing:
			aGame.reset()

		player_one = request.form['user_name']
		player_two = command[1][1:]

		aGame.player_one = player_one
		aGame.player_two = player_two
		aGame.set_turn(player_one)

		return jsonify(
			response_type='in_channel',
			attachments=[
	        {
            "text": "*new game:* " + aGame.player_one + ":x: vs " + aGame.player_two +" :o: \n" + aGame.display_board() + "\n *It's turn: *" + aGame.turn,
            "color": "#3AA3E3",
            "attachment_type": "default"
	        }
	    ]
		)

	elif command[0] == "make_move":
		move = int(command[1])
		outcome = aGame.make_move(move-1, request.form['user_name'])
		if outcome=="":
			return jsonify(
				response_type='in_channel',
				attachments=[
		        {
	            "text": "*Ongoing game:* " + aGame.player_one + ":x: vs " + aGame.player_two +":o: \n" + aGame.display_board() + "\n *It's turn: *" + aGame.turn,
	            "color": "#3AA3E3",
	            "attachment_type": "default"
		        }
		    ]
			)
		elif (outcome == "Please make a valid move!"):
			return jsonify(
				response_type='in_channel',
				attachments=[
		        {
	            "text": "Please make a valid move!\n*Ongoing game:* " + aGame.player_one + ":x: vs " + aGame.player_two +":o: \n" + aGame.display_board() + "\n *It's turn: *" + aGame.turn,
	            "color": "#3AA3E3",
	            "attachment_type": "default"
		        }
		    ]
			)
		elif (outcome=="Ops, you can't make a move right now!"):
			return jsonify(
				response_type='in_channel',
				attachments=[
		        {
		            "text": "Ops, you can't make a move right now!",
		            "color": "#3AA3E3",
		            "attachment_type": "default",
		        }
		    ]
			)

		else:
			if outcome == "Draw":
				return jsonify(
					response_type='in_channel',
					attachments=[
			        {
			            "text": "It's over! Game ended in a draw!",
			            "color": "#3AA3E3",
			            "attachment_type": "default",
			        }
			    ]
				)
			else:
				return jsonify(
					response_type='in_channel',
					attachments=[
			        {
			            "text": "It's over! "+ outcome +" won this match!",
			            "color": "#3AA3E3",
			            "attachment_type": "default",
			        }
			    ]
				)

	elif command[0] == "display":
		if (aGame.ongoing):
			text = "The game currently: \n" + aGame.display_board()
		else:
			text = "There is currently no ongoing game!"
			
		return jsonify(
				response_type='in_channel',
				attachments=[
		        {
	            "text": "The game currently: \n" + aGame.display_board(),
	            "color": "#3AA3E3",
	            "attachment_type": "default"
		        }
		    ]
			)


	elif command[0] == "turn":
		return jsonify(
			response_type='in_channel',
			attachments=[
	        {
	            "text": "It's "+ aGame.turn +"'s to make a move!",
	            "color": "#3AA3E3",
	            "attachment_type": "default",
	        }
	    ]
		)

	elif command[0] == "help":
		possible_commands = "Here are the possible commands you can make with this `/ttt` slash command:\n" \
												"`/ttt turn`: allows you to see which player's turn it is\n" \
												"`/ttt make_move NUMBER`: allows you to make a move on space NUMBER on the board\n" \
												"`/ttt challenge @user`: allows you to start a game with someone in your workplace\n" \
												"`/ttt display`: allows you to view the board of a game if it's ongoing"
		return jsonify(
					response_type='in_channel',
					attachments=[
			        {
			            "text": possible_commands,
			            "color": "#3AA3E3",
			            "attachment_type": "default",
			        }
			    ]
				)
	else:
		return jsonify(
			response_type='in_channel',
			attachments=[
	        {
	            "text": "You typed in an invalid command! Do you need help? Type `/ttt help` for a list of possible commands",
	            "color": "#3AA3E3",
	            "attachment_type": "default",
	        }
	    ]
		)


	return;
		

"""
@app.route('/make-move', methods=['GET'])
def makingGameMove():
	if not valid_request(request):
		abort(400)
"""
	

if __name__ == "__main__":
	app.run('localhost', 80)
