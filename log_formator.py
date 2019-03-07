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
                if data[0][:13] != "date ; stroke":
                    data.insert(0, "date ; stroke\n")
                final_data = []
                for line in data :
                    if (not "Exiting..." in line) and (not "None" in line):
                        try :
                            final_data.append(line.split(' ; ')[0] + ' ; ' + line.split(' ; ')[1].lower())
                        except :
                            continue
                with open(logs_path + filename, "w") as f:
                    f.write('\n'.join(final_data))
                    f.close()
                    print(filename + " overwritten")