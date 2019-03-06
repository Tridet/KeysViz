import codecs
import os
import re

def log2data(logs_path):

    """
    Parse the logs to remove useless lines at the beginning and the end and to add columns name (date, stroke)

    Inputs:
    - logs_path: path of the logs

    Returns:
    - parsed text files
    """

    for filename in os.listdir(logs_path):
        if (re.match(r'^(?!\.).*', filename) and re.match(r'.*\.txt$', filename) and re.match(r'^(?!miserables.txt$)', filename)
                and re.match(r'^(?!christie.txt$)', filename)):
            print("reading "+ filename)
            with codecs.open(logs_path + filename, "r+", encoding='utf-8', errors='ignore') as f:
                #data = f.readlines()
                data = [line.strip() for line in f if line.strip()]
                for k in range(len(data)):
                    data[k] = data[k].replace("◊","crtl+v").replace("≈","ctrl+a").replace("È","é").replace("©","ctrl+c").replace("æ","ctrl+a").replace("˚","°").replace("Ë","è").replace("˘","ù").replace("Â","ctrl+z")
                change1 = False
                change2 = False
                if data[0][:13] != "date ; stroke":
                    data.insert(0, "date ; stroke\n")
                    change1 = True
                last_stroke = data[-1]
                if "Exiting..." in last_stroke:
                    del data[-1]
                    del data[-1]
                    change2 = True

                with open(logs_path + filename, "w") as f:
                    f.write('\n'.join(data))
                    f.close()
                    print(filename + " overwritten")