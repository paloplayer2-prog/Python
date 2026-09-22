import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x550")
window.config(bg="#f0f0f0")

# ==========================================
# 1. SCREEN SWITCHING FUNCTION
# ==========================================
def start_game():
    start_frame.pack_forget()  # 🙈 Hide the Welcome screen
    game_frame.pack()          # 👁️ Show the Game screen


# ==========================================
# 2. GAME LOGIC FUNCTION
# ==========================================
def play(player_choice):
    computer_choice = random.choice(choices)
    choice_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}")

    if player_choice == computer_choice:
        result_label.config(text="It's a Tie! 🤝", fg="gray")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="🎉 YOU WIN! 🎉", fg="green")
    else:
        result_label.config(text="💀 COMPUTER WINS! 💀", fg="red")


# ==========================================
# 3. SCREEN 1: WELCOME / START SCREEN
# ==========================================
start_frame = tk.Frame(window, bg="#f0f0f0")

welcome_title = tk.Label(
    start_frame, 
    text="🎮 Welcome to\nRock Paper Scissors!", 
    font=("Arial", 22, "bold"), 
    bg="#f0f0f0",
)
welcome_title.pack(pady=40)

start_btn = tk.Button(
    start_frame, 
    text="🚀 Start Game", 
    font=("Arial", 16, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    width=14, 
    command=start_game  # Calls our switch function!
)
start_btn.pack(pady=20)

# Show the Start Frame first!
start_frame.pack()


# ==========================================
# 4. SCREEN 2: MAIN GAMEPLAY SCREEN
# ==========================================
game_frame = tk.Frame(window, bg="#f0f0f0")

game_title = tk.Label(game_frame, text="Make Your Move:", font=("Arial", 16, "bold"), bg="#f0f0f0")
game_title.pack(pady=15)

# Choice buttons
rock_btn = tk.Button(game_frame, text="🪨 Rock", font=("Arial", 14), width=12, command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(game_frame, text="📄 Paper", font=("Arial", 14), width=12, command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(game_frame, text="✂️ Scissors", font=("Arial", 14), width=12, command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

# Results
choice_label = tk.Label(game_frame, text="", font=("Arial", 13), bg="#f0f0f0")
choice_label.pack(pady=20)

result_label = tk.Label(game_frame, text="", font=("Arial", 18, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

# (Notice we do NOT pack game_frame here yet—it waits until Start is clicked!)

window.mainloop()