import string
import json
import csv

name = "logs_mail" #nom du logs

##### ATTENTION CHANGER LE DELITMITEUR PEUT ETRE ?????

with open(name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    list_strokes = []
    for row in csv_reader:
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
  
with open(name + '.csv', mode='w') as csv_file:
    fieldnames = ['father', 'son', 'count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for x in new_list:
        writer.writerow(x)
