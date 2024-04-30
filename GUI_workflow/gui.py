import tkinter as tk
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# import itertools
# import threading
# import time
# import sys
# 
# done = False
# #here is the animation
# def animate():
#     for c in itertools.cycle(['|', '/', '-', '\\']):
#         if done:
#             break
#         sys.stdout.write('\rloading ' + c)
#         sys.stdout.flush()
#         time.sleep(0.1)
#     sys.stdout.write('\rDone!     ')
# 
# t = threading.Thread(target=animate)
# t.start()
# 
# #long process here
# time.sleep(10)
# done = True

# tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-base", trust_remote_code=True)
# #add .cuda() for gpu
# model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-1.3b-base", trust_remote_code=True)
# input_text = "add two numbers in fortran"
# inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
# outputs = model.generate(**inputs, max_length=128)
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))

######################################
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

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
    # print("-"*80)
    return tokenizer.decode(outputs[0])
######################################


######################################  * GUI *
def filter_in(str):
    result = ""
    for line in str.splitlines():
        if "<empty_output>" in line:
            result = result + ""  # i.e. don't add to string
        else:
            result = result + line + "\n"
    
    return result

def clear_output():
    output_text.config(state="normal")
    output_text.delete('1.0', tk.END)
    output_text.config(state="disabled")

def get_input(event=None):
    user_input = entry.get()
    # output_text.delete('1.0', tk.END)
    output_text.config(state="normal")
    output_text.insert(tk.END, user_input + "\n")
    model_result = model_generate(user_input)
    output_text.insert(tk.END, filter_in(model_result) + "\n\n\n\n\n\n\n\n")

    # output_text.insert(tk.END, user_input + "\n\n\n\n\n\n\n\n") #### tmp uncomment for only gui testing
    output_text.yview(tk.END)

    output_text.config(state="disabled")
    entry.delete(0, tk.END)  # Clear the entry box after submitting

def get_input_ret(event):
    user_input = entry.get()
    # output_text.delete('1.0', tk.END)
    output_text.config(state="normal")
    output_text.insert(tk.END, user_input + "\n")
    model_result = model_generate(user_input)
    output_text.insert(tk.END, filter_in(model_result) + "\n\n\n\n\n\n\n\n")

    # output_text.insert(tk.END, user_input + "\n\n\n\n\n\n\n\n") #### tmp uncomment for only gui testing
    output_text.yview(tk.END)

    output_text.config(state="disabled")
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
entry.bind('<Return>', get_input_ret)

# Create a frame for the button
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Button widget for submitting input
submit = tk.Button(button_frame, text="Submit", font=('Times New Roman', 20), command=get_input)
submit.pack(side=tk.LEFT)

clear = tk.Button(button_frame, text="Clear", font=('Times New Roman', 20), command=clear_output)
clear.pack(side=tk.RIGHT, padx=25)

# Create a Text widget for displaying output
output_text = tk.Text(root, width=200, height=80, font=('Times New Roman', 20))
output_text.pack(padx=5,pady=5)
output_text.config(state="disabled")

root.mainloop()
