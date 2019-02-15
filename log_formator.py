import codecs
import os
import re

cwd = os.getcwd()
logs_path = cwd+"/data/logs/"

def log2data(logs_path):

    for filename in os.listdir(logs_path):
        if re.match(r'^(?!\.).*', filename):
            with codecs.open(logs_path + filename, "r+", encoding='utf-8', errors='ignore') as f:
                data = f.readlines()
                change1 = False
                change2 = False
                if data[0] != "date ; stroke\n":
                    data.insert(0, "date ; stroke\n")
                    change1 = True
                last_stroke = data[-1].split(";")[1]
                if last_stroke == "Exiting...\n" or last_stroke == "Exiting..." :
                    del data[-1]
                    del data[-1]
                    change2 = True
                if (change1 or change2) :
                    with open(logs_path + filename, "w") as f:
                        print(filename+" overwrite")
                        f.write(''.join(data))
                        f.close
                else:
                    print(filename + " unchanged")


