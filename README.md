Add files via upload
This Python code implements a simple Rock-Paper-Scissors game using the Tkinter library to create a graphical user interface (GUI). The game allows a user to play against the computer, and the application tracks the scores of both the user and the computer. Here's a detailed breakdown of the code:

1. Importing Libraries:
tkinter as tk: Tkinter is used to create the GUI components.
random: The random module is used to allow the computer to make a random choice between Rock, Paper, and Scissors.
2. Game Logic - determine_winner(user_choice):
options: A list of possible choices: Rock, Paper, and Scissors.
computer_choice: The computer randomly selects one of the options.
The function compares the user's choice with the computer's choice to determine the outcome:
If both choices are the same, it's a tie.
If the user wins (based on the rules of Rock-Paper-Scissors), the user score is incremented.
If the computer wins, the computer score is incremented.
Labels Update: The result label, user choice label, computer choice label, and score label are updated to reflect the game's outcome.
3. Resetting the Game - reset_game():
This function resets both the user and computer scores to 0.
It clears the result and choice labels to prepare for a new game.
4. Exiting the Game - exit_game():
This function closes the application by calling root.quit().
5. Creating the Main Window:
root = tk.Tk(): Initializes the main application window.
root.title("Rock Paper Scissors"): Sets the window title.
root.geometry("400x600"): Sets the window size.
root.configure(bg="#F0F0F0"): Configures the background color of the window.
6. Initializing Scores:
user_score and computer_score: These variables are initialized to 0 and are updated as the game progresses.
7. GUI Components:
Header Labels:
1.	The header_label displays the game title.
2.	The sub_header_label indicates that the game is played against AI.
3.	Score Label: score_label shows the current score in the format user_score - computer_score.
4.	Choice Labels: user_choice_label and computer_choice_label display the choices made by the user and the computer, respectively.
5.	Result Label: result_label shows the outcome of each round (e.g., "You Win!" or "You Lose!").
6.	Buttons: Rock, Paper, Scissors Buttons: These buttons allow the user to choose Rock, Paper, or Scissors. Each button triggers the determine_winner() function with the corresponding user choice.
7.	Reset Button: Resets the game, including the scores and labels, to start a new game.
8.	Button Styles: The buttons are styled with colors (e.g., blue for the game choices and red for the reset button) and text formatting to make the interface more visually appealing.
9.	Running the Application: root.mainloop(): This line starts the Tkinter event loop, which keeps the application running and responsive to user input.
10.	User Interaction: The user interacts with the game by clicking on the "Rock," "Paper," or "Scissors" buttons. The computer makes a random choice, and the result of the round is displayed along with the updated score. The user can reset the game at any time using the "Reset" button.

This code provides a simple yet engaging Rock-Paper-Scissors game that demonstrates how to use Tkinter to create a GUI and manage user interaction in a Python application.
