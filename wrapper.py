#!/usr/bin/env python3

import subprocess

command = input('enter command: ')
while command != 'Quit':
    term_command = "make -j && ./main -m models/codellama-7bQ2_K.gguf -p {} -n 400 -e".format(command)
    print(term_command.split())
    result = subprocess.run(
        term_command.split(), 
        capture_output = True,
        text = True
    )

    #process output here
    print(result.stdout)
    print(result.stderr)

    command = input('enter command: ')