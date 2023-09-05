import random

# The possible moves in the game
moves = ["rock", "paper", "scissors"]

# Function to randomly choose a move for the computer
def get_computer_move():
    return random.choice(moves)

# Function to check who won the game
def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif (player_move == "rock" and computer_move == "scissors") or \
        (player_move == "paper" and computer_move == "rock") or \
        (player_move == "scissors" and computer_move == "paper"):
        return "player"
    else:
        return "computer"

# Main function
def main():
    # Get the player's move
    player_move = input("Choose your move: rock, paper, or scissors? ")

    # Get the computer's move
    computer_move = get_computer_move()

    # Get the winner
    winner = get_winner(player_move, computer_move)

    # Render the results in HTML
    html = """
    <html>
        <head>
            <title>Rock Paper Scissors</title>
        </head>
        <body>
            <h1>Rock Paper Scissors</h1>
            <p>You chose: <b>{player_move}</b></p>
            <p>Computer chose: <b>{computer_move}</b></p>
            <p>Winner: <b>{winner}</b></p>
        </body>
    </html>
    """.format(
        player_move=player_move,
        computer_move=computer_move,
        winner=winner
    )

    return html

if __name__ == "__main__":
    # Render the results in HTML and print it to the console
    html = main()
    print(html)
