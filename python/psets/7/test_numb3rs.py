import os
from numb3rs import validate

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
file_path = os.path.join(script_directory, 'data.txt')

with open(file_path, 'r') as file:
    string_list = file.readlines()

    for line in string_list:
        validate(line.strip())
