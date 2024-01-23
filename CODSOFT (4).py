import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

        self.root = tk.Tk()
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("400x300")

        # Label to display instructions and scores
        self.instruction_label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.instruction_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.score_label = tk.Label(self.root, text=f"User: {self.user_score} | Computer: {self.computer_score}", font=("Arial", 12, "bold"))
        self.score_label.grid(row=1, column=0, columnspan=3, pady=5)

        # Buttons for user choices
        choices = ["Rock", "Paper", "Scissors"]
        for i, choice in enumerate(choices):
            button = tk.Button(self.root, text=choice, command=lambda c=choice: self.play_round(c), font=("Arial", 12))
            button.grid(row=2, column=i, padx=10, pady=5)

        # Label to display the result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "italic"))
        self.result_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Button to play again
        play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game, font=("Arial", 12))
        play_again_button.grid(row=4, column=0, columnspan=3, pady=10)

    def play_round(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"User: {user_choice} | Computer: {computer_choice}\nResult: {result}")

        if result == "Win":
            self.user_score += 1
        elif result == "Lose":
            self.computer_score += 1

        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "Win"
        else:
            return "Lose"

    def update_score(self):
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def reset_game(self):
        self.result_label.config(text="")
        self.instruction_label.config(text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.user_score = 0
        self.computer_score = 0
        self.update_score()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.root.mainloop()
