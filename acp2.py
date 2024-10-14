import random
import tkinter as tk
from tkinter import messagebox

# Game Logic Function
def play_rps(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    # Determine the result
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        result = 'You win!'
    else:
        result = 'You lose!'
    
    # Update labels
    player_label.config(text=f"Player: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=f"Result: {result}")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")

# Labels for displaying choices and result
player_label = tk.Label(root, text="Player: ", font=("Arial", 12))
player_label.pack()

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack()

# Buttons for player choices
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: play_rps('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: play_rps('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: play_rps('Scissors'))
scissors_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
