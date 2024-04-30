#!/usr/bin/env python3

import subprocess
import os

command = input('enter command: ')
while command != 'Quit':
    term_command = "make -j && ./main -m ./../llama.cpp/models/codellama-70b-hf.Q5_K_M.gguf -p \"{}\" -n 400 -e".format(command)
    os.system(term_command)
    result = subprocess.run(
        term_command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    #process output here
    #print(result.stdout)
    #print(result.stderr)

    command = input('enter command: ')
