import tkinter as tk
import random

# Game logic to determine the winner
def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        global user_score
        user_score += 1
    else:
        result = "You Lose!"
        global computer_score
        computer_score += 1

    # Update labels with results and scores
    result_label.config(text=result, fg="red" if result == "You Lose!" else "green")
    user_choice_label.config(text=f"Human: {user_choice}")
    computer_choice_label.config(text=f"AI: {computer_choice}")
    score_label.config(text=f"{user_score} - {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    score_label.config(text=f"{user_score} - {computer_score}")

# Function to exit the game
def exit_game():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x600")
root.configure(bg="#F0F0F0")

# Initialize scores
user_score = 0
computer_score = 0

# Header label
header_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#F0F0F0", fg="#4A4A4A")
header_label.pack(pady=10)

# Sub-header label
sub_header_label = tk.Label(root, text="With Artificial Intelligence", font=("Helvetica", 12), bg="#F0F0F0", fg="#4A4A4A")
sub_header_label.pack(pady=5)

# Score label
score_label = tk.Label(root, text=f"{user_score} - {computer_score}", font=("Helvetica", 24, "bold"), bg="#F0F0F0", fg="#4A4A4A")
score_label.pack(pady=10)

# Labels to show choices
user_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#F0F0F0", fg="#4A4A4A")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#F0F0F0", fg="#4A4A4A")
computer_choice_label.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#F0F0F0")
result_label.pack(pady=20)

# Buttons for user to select rock, paper, or scissors
button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=8, font=("Helvetica", 14), bg="#4A90E2", fg="white",
                        command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(button_frame, text="Paper", width=8, font=("Helvetica", 14), bg="#4A90E2", fg="white",
                         command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=8, font=("Helvetica", 14), bg="#4A90E2", fg="white",
                            command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Reset button to start a new game
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_game, bg="#E74C3C", fg="white")
reset_button.pack(pady=10)

# Run the main event loop
root.mainloop()
