import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("800x800+0+0")
root.title("Fortran Coder")
root.configure(background="lightgray")

entry = tk.Entry(root, width=50)
entry.pack()

resFrame = tk.Frame(root, height=400, width=200, background="white")
resFrame.place(x=0, y=0)
resFrame.grid_propagate(0)

result = ttk.Label(resFrame, text="Testing")
result.pack()


root.mainloop()