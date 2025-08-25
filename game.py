import tkinter as tk      # tk short name banane ke liye
from tkinter import ttk   # ttk ka alag se import (optional)
import random
w = tk.Tk() 
w.title("Stone Paper and Scissor Game") 
w.geometry("1200x700") 
w.configure(bg="light blue") 
# ------------ considered to be constants ------------------- 
CHOICES = ["Stone","Paper","Scissor"] 
WIN_PAIRS = { 
    ("Stone", "Scissor"), 
    ("Paper", "Stone"),
    ("Scissor", "Paper"),
} 
# defining all the functions 
def play(user_choice: str): 
    cpu_choice = random.choice(CHOICES)
    # """Ek round khelo: user_choice aaya, ab cpu choose karega, result nikaalo.""" 
    # UI pe choices set karo 
    w.user_pick.set(user_choice) 
    w.cpu_pick.set(cpu_choice) 
    
    #result determination: 
    if (user_choice == cpu_choice): 
        w.result_msg.set("It's a Tie! 😐") 
        _set_result_color("grey") 
    elif(user_choice,cpu_choice) in WIN_PAIRS: 
        w.result_msg.set("You Win! 🎉")
        w.user_score.set(w.user_score.get() + 1)
        _set_result_color("green") 
    else: 
        w.result_msg.set("You Lose! 😢")
        w.user_score.set(w.cpu_score.get() + 1)
        _set_result_color("red") 

def reset():
    "Reset all the scores" 
    w.user_score.set(0) 
    w.cpu_score.set(0) 
    w.user_pick.set("-") 
    w.cpu_pick.set("-") 
    w.result_msg.set("Scores reset. Play again!") 
    w._set_result_color("#000000") 
# top title 
L1 = tk.Label(w, text="Stone <-> Paper <-> Scissor", font=("Segoe UI", 20, "bold"), bg="light blue") 
L1.pack(pady=(18, 8)) 
# ---------- Game State ---------- 
w.user_score = tk.IntVar(value=0) # User ke points 
w.cpu_score = tk.IntVar(value=0) # Computer ke points 
w.user_pick = tk.StringVar(value="-")# User ne kya choose kiya 
w.cpu_pick = tk.StringVar(value="-")# CPU ne kya choose kiya 
w.result_msg = tk.StringVar(value="Click a button to start!") 

# scoreboard for user and cpu 
score_frame = tk.Frame(w, bg = "light blue") 
score_frame.pack(pady=20) 

user_lbl = tk.Label(score_frame, text="You", font=("Segoe UI", 12, "bold"), bg = "light blue") 
user_lbl.grid(row=0, column=0, padx=12, pady=2) 

user_score = tk.Label(score_frame, textvariable=w.user_score, font=("Consolas", 18, "bold"), bg = "light blue") 
user_score.grid(row=1, column=0, padx=12, pady=10) 

L3 = tk.Label(score_frame, text="VS", font=("Segoe UI", 12), bg = "light blue") 
L3.grid(row=1, column=1, padx=10) 

cpu_lbl = tk.Label(score_frame, text="Computer", font=("Segoe UI", 12, "bold"), bg = "light blue") 
cpu_lbl.grid(row=0, column=2, padx=30, pady=2) 

cpu_score = tk.Label(score_frame, textvariable=w.cpu_score, font=("Consolas", 18, "bold"), bg = "light blue") 
cpu_score.grid(row=1, column=2, padx=12, pady=10) 

# pick frame(who choses waht) 
pick_frame = tk.Frame(w, bg = "light blue") 
pick_frame.pack(pady=20)

user_pick = tk.Label(pick_frame, text="Your pick:", font=("Segoe UI", 11), bg = "light blue") 
user_pick.grid(row=0, column=0, padx=6) 
user_pick = tk.Label(pick_frame, textvariable=w.user_pick, font=("Segoe UI", 15, "bold"), bg = "light blue").grid(row=0, column=1, padx=6) 

cpu_pick = tk.Label(pick_frame, text="Computer pick:", font=("Segoe UI", 11), bg = "light blue") 
cpu_pick.grid(row=0, column=2, padx=15) 
cpu_pick = tk.Label(pick_frame, textvariable=w.cpu_pick, font=("Segoe UI", 15, "bold"), bg = "light blue").grid(row=0, column=3, padx=6) 

# Buttons Frame 
btns_frame = tk.Frame(w, bg = "light blue") 
btns_frame.pack(pady=10) 

# Har button ka command: lambda me specific choice 
stone_btn = tk.Button(btns_frame, text="🪨 Stone", font=("Segoe UI", 20, "bold"), width=12, 
                      command=lambda: play("Stone"), bg = "light blue").grid(row=0, column=0, padx=8, pady=6) 
paper_btn = tk.Button(btns_frame, text="📄 Paper", font=("Segoe UI", 20, "bold"), width=12, 
                      command=lambda: play("Paper"), bg = "light blue").grid(row=0, column=1, padx=8, pady=6) 
sciccor_btn = tk.Button(btns_frame, text="✂️ Scissor", font=("Segoe UI", 20, "bold"), width=12, 
                        command=lambda: play("Scissor"), bg = "light blue").grid(row=0, column=2, padx=8, pady=6) 

# result display 
result_lbl = tk.Label(w, textvariable = w.result_msg,font=("Segoe UI", 12, "bold")) 
result_lbl.pack(pady=(8, 4)) 

# Reset button(to reset all the scores) 
reset_btn = tk.Button(w,text="Reset", font=("Segoe UI", 10), bg = "light blue", 
                      command=reset) 
reset_btn.pack(pady=(2, 10)) 
# # if we write both the statement in one line then it will return None 

# winning criteria 
w_c = tk.Label(w,text="First to reach score 5 will win the match 😊", 
               font=("Segoe UI",8),fg="red", bg="light blue") 
w_c.pack() 

def _set_result_color(color_hex: str):
    
        # """Result label ka text color badlo (feedback ke liye)."""
    w.result_label.config(fg=color_hex)

w.mainloop()