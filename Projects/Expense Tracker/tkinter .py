from tkinter import *

win = Tk()

win.title("Graphical User Interface")
win.geometry("400x600")

tf = Frame(win,  bg="Grey",height=100)
tf.pack()

tl = Label(tf,text= "TOP FRAME",height=50)
tl.pack(pady=10)

tf = Frame(win, bg="lightblue", height=100)
tf.pack(fill="x")

bf = Frame(win, bg="lightgreen", height=200)
bf.pack(fill="x")

tl = Label(tf, text="TOP FRAME", bg="lightblue")
tl.pack(pady=20)

bl = Label(bf, text="BOTTOM FRAME", bg="lightgreen")
bl.pack(pady=30)


win.mainloop()