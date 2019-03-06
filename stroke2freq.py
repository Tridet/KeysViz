import os
from log_formator import log2data
import re
import pandas as pd
import json

cwd = os.getcwd()
logs_path = cwd+"/data/logs/"


def stroke2freq(logs_path):

    """
    Create a json file with the number of occurences for each stroke for each category of logs

    Inputs:
    - logs_path: path of the logs

    Returns:
    - data.json
    """

    freq = {}
    for filename in os.listdir(logs_path):
        if (re.match(r'^(?!\.).*', filename) and re.match(r".*\.txt$", filename)):
            data = pd.read_csv(logs_path + filename, sep=' ; ', engine='python')
            counts = data['stroke'].value_counts().to_dict()
            list_key = ['Exiting...', 'None']
            for key in list_key:
                counts.pop(key, None)
            main_key = filename.split('.')[0]
            freq[main_key] = counts

    dict_all = {}
    for dicts in freq:
        for key in freq[dicts]:
            if key not in dict_all:
                dict_all[key] = freq[dicts][key]
            else:
                dict_all[key] = dict_all[key] + freq[dicts][key]
    freq["all"] = dict_all
    with open('data.json', 'w') as outfile:
        json.dump(freq, outfile)
