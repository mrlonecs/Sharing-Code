import tkinter as tk
import time

def start_timer(entry, label):
    try:
        seconds = int(entry.get())
        while seconds > 0:
            label.config(text=f"Time remaining: {seconds} seconds")
            root.update()  # Force update
            time.sleep(1)
            seconds -= 1
        label.config(text="Time's up!")
    except ValueError:
        label.config(text="Enter a valid number!")

def open_new_window():
    new_win = tk.Toplevel(root)
    new_win.title("Another Timer")

    tk.Label(new_win, text="Enter seconds:").pack()
    entry = tk.Entry(new_win)
    entry.pack()

    label = tk.Label(new_win, text="")
    label.pack(pady=10)

    tk.Button(new_win, text="Start", command=lambda: start_timer(entry, label)).pack()

root = tk.Tk()
root.title("Main Timer")

tk.Label(root, text="Enter seconds:").pack()
entry_main = tk.Entry(root)
entry_main.pack()

label_main = tk.Label(root, text="")
label_main.pack(pady=10)

tk.Button(root, text="Start Timer", command=lambda: start_timer(entry_main, label_main)).pack()
tk.Button(root, text="Open Another Timer", command=open_new_window).pack(pady=10)

root.mainloop()
