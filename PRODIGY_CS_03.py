import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password = entry.get()

    strength_points = 0
    feedback = []

    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("• Minimum 8 characters required")

    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("• Add an uppercase letter")

    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("• Add a lowercase letter")

    if re.search(r"\d", password):
        strength_points += 1
    else:
        feedback.append("• Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        feedback.append("• Add a special character")

    if strength_points == 5:
        result = "Very Strong Password ✅"
        color = "green"
    elif strength_points == 4:
        result = "Strong Password 🟢"
        color = "blue"
    elif strength_points == 3:
        result = "Medium Password 🟡"
        color = "orange"
    else:
        result = "Weak Password 🔴"
        color = "red"

    result_label.config(text=result, fg=color)

    feedback_text.delete("1.0", tk.END)

    if feedback:
        feedback_text.insert(tk.END, "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "Excellent! Your password is secure.")

root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("500x400")
root.config(bg="#1e1e2f")

title = tk.Label(
    root,
    text="Password Complexity Checker",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

entry = tk.Entry(root, width=30, font=("Arial", 14), show="*")
entry.pack(pady=10)


check_btn = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=check_password
)
check_btn.pack(pady=10)


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=10)


feedback_text = tk.Text(
    root,
    height=8,
    width=45,
    font=("Arial", 11)
)
feedback_text.pack(pady=10)

root.mainloop()