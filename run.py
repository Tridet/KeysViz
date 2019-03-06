from log_formator import log2data
from stroke2freq import stroke2freq
from chords_data_parsing import chords_data_parsing
import os

cwd = os.getcwd()
logs_path = cwd+"/data/logs/"

if __name__ == '__main__':
    log2data(logs_path)
    stroke2freq(logs_path)
    chords_data_parsing(logs_path)