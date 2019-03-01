import string
import json
import csv
import os
import re
import pandas as pd

cwd = os.getcwd()
logs_path = cwd+"/data/logs/"

def chords_data_parsing(logs_path):
    for filename in os.listdir(logs_path):
        if (re.match(r'^(?!\.).*', filename) and re.match(r".*\.txt$", filename)):
            with open(logs_path + filename) as csv_file:
                csv_reader = pd.read_csv(csv_file, sep=' ; ', engine='python')
                line_count = 0
                list_strokes = []
                for index, row in csv_reader.iterrows():
                    list_strokes.append(row[1])
                    line_count += 1

            for i in range(len(list_strokes)):
                list_strokes[i] = list_strokes[i].replace(" ", "").lower()

            hierarchical_list = []
            alphabet = list(string.ascii_lowercase)
            is_in_dic = []

            for i in range(len(list_strokes)-1):
                if list_strokes[i] in alphabet and list_strokes[i+1] in alphabet:
                    if list_strokes[i] in is_in_dic:
                        a = False
                        count = 0
                        while not(a) and count < len(hierarchical_list):
                            if hierarchical_list[count]["name"] == list_strokes[i]:
                                if not(list_strokes[i+1] in hierarchical_list[count]["list_children"]):
                                    hierarchical_list[count]["children"].append({"name" : list_strokes[i+1], "value" : 1})
                                    hierarchical_list[count]["list_children"].append(list_strokes[i+1])
                                else:
                                    for j in range(len(hierarchical_list[count]["children"])):
                                        if hierarchical_list[count]["children"][j]["name"] == list_strokes[i+1]:
                                            hierarchical_list[count]["children"][j]["value"] += 1
                                a = True
                            count+=1
                    else:
                        dic = {"name" : list_strokes[i], "children" : [{"name" : list_strokes[i+1], "value" : 1}], "list_children" : [list_strokes[i+1]]}
                        hierarchical_list.append(dic)
                        is_in_dic.append(list_strokes[i])

            new_list = []

            for i in range(len(hierarchical_list)):
                for j in range(len(hierarchical_list[i]["children"])):
                    new_list.append({"father" : hierarchical_list[i]["name"], "son" : hierarchical_list[i]["children"][j]["name"], "count" : hierarchical_list[i]["children"][j]["value"]})

            new_filename = filename.split(".txt")[0]
            with open(logs_path + new_filename + '_bigram.csv', mode='w') as csv_file:
                fieldnames = ['father', 'son', 'count']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for x in new_list:
                    writer.writerow(x)

#chords_data_parsing(logs_path)