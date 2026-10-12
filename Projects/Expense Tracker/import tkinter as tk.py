import tkinter as tk

win = tk.Tk()
win.title("CE Online Class")
win.geometry("400x300")

def on_click():
    name = te.get()
    color = te2.get()
    tl.config(
        text=name,
        bg=color,
        fg="White",
        font=("Times New Roman", 20)
    )

tf = tk.Frame(win, bg="lightblue", height=100)
tf.pack(fill="x")

bf = tk.Frame(win, bg="lightgreen", height=200)
bf.pack(fill="x")

tl = tk.Label(tf, text="TOP FRAME", bg="lightblue")
tl.pack(pady=20)

bl = tk.Label(bf, text="BOTTOM FRAME", bg="lightgreen")
bl.pack(pady=50)

te = tk.Entry(tf)
te.pack(pady=20)

te2 = tk.Entry(tf)
te2.pack(pady=10)

bb = tk.Button(
    bf,
    text="Click Me!",
    bg="lightgreen",
    command=on_click
)
bb.pack()

win.mainloop()