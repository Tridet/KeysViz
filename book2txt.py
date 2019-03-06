import string
import json
import csv
import os
import re
import codecs
import pandas as pd

cwd = os.getcwd()
#book_path = cwd+"/data/LesMiserables/"
book_path = cwd+"/data/AgathaChristie/"
logs_path = cwd+"/data/logs/"

def book2txt(book_path, logs_path, new_filename):

    """
    Parse a book under text format and return a file where each line correspond to a letter (or space) of the book

    Inputs:
    - logs_path: path of the logs
    - book_path: path of the book
    - new_filename : name of the file to be written

    Returns:
    - text file
    """

    characters = []
    for filename in os.listdir(book_path):
        if (re.match(r'^(?!\.).*', filename) and re.match(r".*\.txt$", filename)):
            with codecs.open(book_path + filename, "r+", encoding='utf-8', errors='ignore') as f:
                lines = [line.strip() for line in f if line.strip()]
                for line in lines:
                    line = line.lower()
                    for char in line:
                        if char == ' ':
                            char = 'space'
                        characters.append(char)
    with open(logs_path + new_filename, mode='w') as f:
        f.write('date ; stroke\n')
        for char in characters:
            line = 'nan ; '+ char + '\n'
            f.write(line)
        f.close()
    print(new_filename + " written")

#new_filename = "miserables.txt"
new_filename = "christie.txt"

book2txt(book_path, logs_path, new_filename)