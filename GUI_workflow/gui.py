import tkinter as tk
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

import itertools
import threading
import time
import sys

# done = False
# def animate():
#     for c in itertools.cycle(['|', '/', '-', '\\']):
#         if done:
#             break
       
#         load.config(text=c)
#         root.update()

#         time.sleep(0.15)

# def animation(process) :
#     while process.is_alive():
#         chars = ['|', '/', '-', '\\']
#         for c in chars:
#             load.config(text=c)
#             time.sleep(0.15)

# tester function TODO: remove
def long_running_computation(target_time):
    start_time = time.time()
    i = 1
    result = 0
    while time.time() - start_time < target_time:
        result += i**2
        i += 1
    return result

# model generation
def model_generate(user_prompt):
    # generate model result using prompt
    checkpoint = "smallcloudai/Refact-1_6B-fim"
    # "cuda" for gpu
    device = "cpu" 

    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True).to(device)

    prompt_template = "<empty_output>SYSTEM {system}\n<empty_output>USER {query}\n<empty_output>ASSISTANT"

    prompt = prompt_template.format(system="You are a programming assistant",
                                    query=user_prompt)

    inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
    outputs = model.generate(inputs, max_length=1000, temperature=0.2)
    return tokenizer.decode(outputs[0])


# filter output from model
def filter_in(str):
    result = ""
    for line in str.splitlines():
        if "<empty_output>" in line:
            result = result + ""  # i.e. don't add to string
        else:
            result = result + line + "\n"
    
    return result

# clear textbox containing model results
def clear_output():
    output_text.config(state="normal")
    output_text.delete('1.0', tk.END)
    output_text.config(state="disabled")

# helper function for loading and generating model results
def loading(event=None):
    load.config(text="Loading . . .")
    # time.sleep(0.5)
    root.update()
    get_input()

# second helper function (used when 'Enter' submits user prompt)
def loading2(event):
    load.config(text="Loading . . .")
    # time.sleep(0.5)
    root.update()
    get_input()


# function connecting user submission with model generation
def get_input():
    # done = False
    # a = threading.Thread(target=animate, daemon=False)
    # a.start()
    # root.update()
    

    # animation(the_process)
    # animate()
    # the_process_function()
    # the_process.join()
    # long_running_computation(3)
    # time.sleep(3)
    # done = True
    # output_text.insert(tk.END, "end of computation") 
    

    user_input = entry.get()
    # output_text.delete('1.0', tk.END)
    output_text.config(state="normal")
    output_text.insert(tk.END, user_input + "\n")
    model_result = model_generate(user_input)
    output_text.insert(tk.END, filter_in(model_result) + "\n\n\n\n\n\n\n\n")

    load.config(text=" ")
    root.update()
    #long process here
    # entry.delete('1.0', tk.END)

    # the_process_function()
    # time.sleep(10)
    done = True

    # output_text.insert(tk.END, user_input + "\n\n\n\n\n\n\n\n") #### tmp uncomment for only gui testing
    output_text.yview(tk.END)

    output_text.config(state="disabled")
    entry.delete(0, tk.END)  # Clear the entry box after submitting
    load.config(text=" ")


# * GUI * #
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
entry.bind('<Return>', loading2)

# Create a frame for the button
h_frame = tk.Frame(root)
h_frame.pack(pady=5)

load_frame = tk.Frame(h_frame, padx=10)
load_frame.grid(row=0, column=0)

button_frame = tk.Frame(h_frame)
button_frame.grid(row=0, column=1)

empty_frame = tk.Frame(h_frame, width=100)
empty_frame.grid(row=0, column=3)

load = tk.Label(load_frame, text=" ", width=20, font=('Times New Roman', 20))
load.pack(side=tk.LEFT)

# Button widget for submitting input
submit = tk.Button(button_frame, text="Submit", font=('Times New Roman', 20), command=loading)
submit.pack(side=tk.LEFT)

clear = tk.Button(button_frame, text="Clear", font=('Times New Roman', 20), command=clear_output)
clear.pack(side=tk.RIGHT, padx=25)

# Create a Text widget for displaying output
output_text = tk.Text(root, width=200, height=80, font=('Times New Roman', 20))
output_text.pack(padx=5,pady=5)
output_text.config(state="disabled")

root.mainloop()
