import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # GUI Components
        self.user_label = ttk.Label(root, text="Your Choice:")
        self.user_label.grid(row=0, column=0, padx=10, pady=5)

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")
        self.user_choice_dropdown = ttk.Combobox(root, textvariable=self.user_choice_var, values=["rock", "paper", "scissors"])
        self.user_choice_dropdown.grid(row=0, column=1, padx=10, pady=5)

        self.play_button = ttk.Button(root, text="Play", command=self.play_game)
        self.play_button.grid(row=0, column=2, padx=10, pady=5)

        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.grid(row=1, column=0, columnspan=3, pady=5)

        self.score_label = ttk.Label(root, text="Scores - You: 0, Computer: 0")
        self.score_label.grid(row=2, column=0, columnspan=3, pady=5)

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"Result: {result}")

        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

        self.score_label.config(text=f"Scores - You: {self.user_score}, Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
