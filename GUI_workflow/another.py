import tkinter as tk

def get_input():
    user_input = entry.get()
    # output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, user_input + "\n")
    output_text.insert(tk.END, "================================================================================================================================" + "\n\n\n")
    entry.delete(0, tk.END)  # Clear the entry box after submitting

root = tk.Tk()
root.title("Fortran Code Generator")

# Create a frame for the input section
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Label and Entry widgets for input
label = tk.Label(input_frame, text="Prompt:", font=('Times New Roman', 20))
label.pack(side=tk.LEFT)

entry = tk.Entry(input_frame, width=100, font=('Times New Roman', 20))
entry.pack(side=tk.LEFT)

# Create a frame for the button
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Button widget for submitting input
button = tk.Button(button_frame, text="Submit", font=('Times New Roman', 20), command=get_input)
button.pack()

# Create a Text widget for displaying output
output_text = tk.Text(root, width=200, height=80, font=('Times New Roman', 20))
output_text.pack(padx=5,pady=5)

root.mainloop()
