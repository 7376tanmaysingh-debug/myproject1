import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
root = tk.Tk()
root.title("IPL Data Analysis")
root.geometry("500x300")
def open_file():
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    df = pd.read_csv(file)
    team_wins = df["winner"].value_counts()
    result.config(
        text="Most Successful Team:\n" +
             team_wins.idxmax() +
             " (" + str(team_wins.max()) + " Wins)"
    )
    team_wins.plot(kind="bar")
    plt.title("Team Wins")
    plt.xlabel("Teams")
    plt.ylabel("Wins")
    plt.show()
    player_runs = df.groupby("Player of The Match")["Total Runs"].sum()
    print(player_runs)
    player_runs.plot(kind="bar")
    plt.title("Player Runs")
    plt.xlabel("Players")
    plt.ylabel("Runs")
    plt.show()
heading = tk.Label(root, text="IPL DATA ANALYSIS", font=("Arial", 18, "bold"))
heading.pack(pady=20)
button = tk.Button(root, text="Upload IPL CSV File", command=open_file)
button.pack(pady=10)
result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)
root.mainloop()