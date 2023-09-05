import random

# Define the game options
options = ["rock", "paper", "scissors"]

# Define the game function
def play_game(request):
    # Get player choice
    player_choice = request.POST["choice"]

    # Validate player choice
    if player_choice not in options:
        return {"message": "Invalid choice."}

    # Get computer choice
    computer_choice = random.choice(options)

    # Print choices
    return {
        "message": "Player: " + player_choice + ", Computer: " + computer_choice,
        "winner": "tie" if player_choice == computer_choice else (
            "you" if player_choice == "rock" and computer_choice == "scissors"
            or player_choice == "paper" and computer_choice == "rock"
            or player_choice == "scissors" and computer_choice == "paper"
            else "computer"
        ),
    }

# Create an app
app = Flask(__name__)

# Add the game route
app.route("/rock_paper_scissors")(play_game)

# Run the app
app.run()
