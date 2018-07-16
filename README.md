# slack-tic-tac-toe
a tic tac toe game via slack!

## slack workplace url
https://slacktictactoe.slack.com

## tutorials to look at:
- https://www.programmableweb.com/news/how-to-use-slack-api-to-build-slash-commands-powered-google-app-engine-and-go/how-to/2015/09/16
- https://api.slack.com/tutorials/easy-peasy-slash-commands
- https://api.slack.com/tutorials/your-first-slash-command

## currently:
[ ] fix display game board command
[ ] A channel can have at most one game being played at a time.
[x] Users can create a new game in any Slack channel by challenging another user (using their @username).
[ ] Anyone in the channel can run a command to display the current board and list whose turn it is.
[ ] ~Users can specify their next move, which also publicly displays the board in the channel after the move~ with a reminder of whose turn it is.
[x] Only the user whose turn it is can make the next move.
[x] When a turn is taken that ends the game, the response indicates this along with who won.


## screenshots:

## how to run
to run listening socket: `ngrok.exe http 80`

## tutorials & code examples used:
- https://github.com/slackapi/python-dialog-example/blob/master/example.py
- https://renzo.lucioni.xyz/serverless-slash-commands-with-python/