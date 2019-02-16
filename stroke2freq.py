import os
from log_formator import log2data
import re
import pandas as pd
import json

cwd = os.getcwd()
logs_path = cwd+"/data/logs/"
#log2data(logs_path)

def stroke2freq(logs_path):
    freq = {}
    for filename in os.listdir(logs_path):
        if re.match(r'^(?!\.).*', filename):
            data = pd.read_csv(logs_path + filename, sep=' ; ', engine='python')
            counts = data['stroke'].value_counts().to_dict()
            list_key = ['Exiting...', 'None']
            for key in list_key:
                counts.pop(key, None)
            main_key = filename.split('.')[0]
            freq[main_key] = counts
            with open('data.json', 'w') as outfile:
                json.dump(freq, outfile)


#stroke2freq(logs_path)