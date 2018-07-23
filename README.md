# slack-tic-tac-toe
a tic tac toe game via slack!

## slack workplace url
https://slacktictactoe.slack.com

## possible slack commands:
- `/ttt turn`: allows you to see which player's turn it is
- `/ttt make_move NUMBER`: allows you to make a move on space NUMBER on the board
- `/ttt challenge @user`: allows you to start a game with someone in your workplace
- `/ttt display`: allows you to view the board of a game if it's ongoing
- `/ttt help`: displays a set of commands you can make

## pains, issues, and thoughts
- One of the earlier issues I had that made my progress to 1.5 days long is figuring out how to send messages. I was following <a href="https://renzo.lucioni.xyz/serverless-slash-commands-with-python/">Renzo Lucioni's</a> tutorial at first and couldn't figure out my issue until I realized my Flask application wasn't listening on the same port as `ngrok`. I also tried to incorporate <a href="https://api.slack.com/docs/message-buttons">interactive message buttons</a> into my tic tac toe board but forgo the idea once I discovered the buttons added a layer of complexity I currently didn't have the time for.

- Figuring out how to track the games being played in different channels proved to be a difficult task. At first I created each game as its own object, the object and method definitions were outlined in `game.py` (this can be explained in data modeling section). But this initial approach didn't account for users being able to create games in multiple channels and I realized I wasn't able to keep track of the object directly in `tracker.py`. With more time, I would probably find a way but I discovered a lot of the attributes I was using in `tracker.py` were also outlined in my original `game.py` file. Thus, I decided it was best to simply have a dictionary, that tracks the status and data of games in different channels and have helper functions in `tracker.py` file, and make all the object methods its own functions to call upon in `game.py` so that I don't repeat methods.

- Given that I've already taken a lot of time, I didn't take into account for some edge cases, such as if the formatting for `/ttt turn` was incorrect.

## data modeling
- A game is being tracked by the channel its in:
	```javascript
		channels : {
			channel_id: {
				'ongoing': BOOLEAN,
				'players': ARRAY,
				'winner': STRING,
				'turn': players[0], // initializing to the first player
				'board': [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
			}
		}
	```
- My original solution was to instantiate a game object, which was outlined in `game.py`:
	```python
		class TicTacToe
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
	```

## screenshots:

### challenging someone
<img src="https://i.gyazo.com/8fd865fb5d31ed170141df4213085760.png" width="400">

### making a move
<img src="https://i.gyazo.com/b1d837fc16d4adc092f921884fbb311b.png" width="400">

### when someone wins
<img src="https://i.gyazo.com/ce1839f43fff741f87862e5a0e80ff0d.png" width="400">

### when someone tries to join a game they're not a part of
<img src="https://i.gyazo.com/b15435b4f7b3965ca1607b178cb4d3f5.png" width="400">

### when someone makes a move when it's not their turn
<img src="https://i.gyazo.com/3169582160ff08a7d2561c66ed2838ec.png" width="400">

### when someone wants to display the board and there is no ongoing game
<img src="https://i.gyazo.com/54cc45a79b01ac342d8d0c7598111ede.png" width="400">

### when someone wants to display the board and there is an ongoing game
<img src="https://i.gyazo.com/4aa455f165fd4558ef4608cf09ff86e3.png" width="400">

### when the game ends in a draw
<img src="https://i.gyazo.com/17ef4d0ad8b5f8cc3efbe31d48cd9bac.png" width="400">

## how to run
1. Run a listening socket via ngrok: `ngrok.exe http 80`
2. Get the forwarding URL and append `/command` and apply in Slack API
4. Run `python main.py`

## tutorial used:
- https://renzo.lucioni.xyz/serverless-slash-commands-with-python/

## time spent
≤1 day
