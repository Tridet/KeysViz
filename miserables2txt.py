import string
import json
import csv
import os
import re
import codecs
import pandas as pd

cwd = os.getcwd()
miserables_path = cwd+"/data/LesMiserables/"
logs_path = cwd+"/data/logs/"

def miserables2txt(miserables_path, logs_path):
    characters = []
    for filename in os.listdir(miserables_path):
        if (re.match(r'^(?!\.).*', filename) and re.match(r".*\.txt$", filename)):
            with codecs.open(miserables_path + filename, "r+", encoding='utf-8', errors='ignore') as f:
                lines = [line.strip() for line in f if line.strip()]
                for line in lines:
                    for char in line:
                        if char == ' ':
                            char = 'space'
                        characters.append(char)
    new_filename = 'miserables.txt'
    with open(logs_path + new_filename, mode='w') as f:
        f.write('date ; stroke\n')
        for char in characters:
            line = 'nan ; '+ char + '\n'
            f.write(line)
        f.close()
    print(new_filename + " written")

#miserables2txt(miserables_path, logs_path)