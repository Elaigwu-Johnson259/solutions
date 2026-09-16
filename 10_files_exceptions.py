#Date: 16-9-2026
# TODO: Exercise 1
# Create a text file named 'learning.txt' inside this directory with three lines:
# "I am learning Python."
# "I am learning file handling."
# "I am learning exception handling."
# Then write code below that reads this file and prints the content all at once.

#solution
with open('learning.txt', 'r') as file:
    content = file.read()
    print(content)


# TODO: Exercise 2
# Write code that appends a fourth line: "I am learning to write code." to 'learning.txt'.
# Then read the file line by line, printing each line stripped of extra whitespace.

#solution
with open('learning.txt', 'a') as file:
    added_line = file.write("\nI am learning to write code.")
    print(added_line) 

with open('learning.txt', 'r') as file:
    for line in file:
        print(line.strip()) 


# TODO: Exercise 4
# Given the dictionary 'config' below, write it to a file named 'config.json' in JSON format.
# Then load it back and print the loaded dictionary.

#solution

import json
config = {"theme": "dark", "volume": 80, "debug_mode": True}
with open("config.json", 'w') as file:
    json.dump(config, file, indent=4)

with open("config.json", 'r') as file:
    loaded_config = json.load(file)
    print(loaded_config)


# TODO: Exercise 3
# Write a try-except block that attempts to open a non-existent file named 'missing.txt'.
# Handle the FileNotFoundError by printing "The file could not be found." instead of crashing.

#solution
try:
    with open('Missing.txt', 'r') as file:
        open_it = file.read()

except FileNotFoundError:
    print('The file could not be found.')