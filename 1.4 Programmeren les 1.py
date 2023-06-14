import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    global beurten_over

    poging = entry.get()

    if len(poging) != 6:
        messagebox.showinfo("Het woord moet precies 6 letters lang zijn.")
        return

    if poging == te_raden_woord:
        messagebox.showinfo("Gefeliciteerd", "Je hebt het woord geraden.")
        root.destroy()
        return

    hint = ""
    for i in range(len(poging)):
        if poging[i] == te_raden_woord[i]:
            hint += poging[i]
        else:
            hint += "_"

    hint_label.config(text="Hint: " + hint)
    beurten_over -= 1

    if beurten_over == 0:
        messagebox.showinfo("Helaas", "Je hebt het woord niet geraden. Het woord was: " + te_raden_woord)
        root.destroy()

lijst_van_woorden = ["Python", "Detail", "Thread", "Sector", "Sodium"]
te_raden_woord = random.choice(lijst_van_woorden)

beurten_over = 5

root = tk.Tk()
root.title("Lingo")

instruction_label = tk.Label(root, text="Het te raden woord heeft 6 letters.")
instruction_label.pack()

guess_label = tk.Label(root, text="Doe een poging:")
guess_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack()

hint_label = tk.Label(root, text="Hint: ")
hint_label.pack()

root.mainloop()











