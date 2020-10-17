import json
import pickle
from tqdm import tqdm
data = {}
data['occurrences'] = []
outAs = 'jsosn'


def loadFile(fileName):
    file = open(fileName, 'r')
    return file.readlines()


def dumpJson(fileName, _json):
    file = open(fileName, 'w')
    json.dump(_json, file, indent=4, sort_keys=True)


def dumpPickle(fileName, _pickle):
    file = open(fileName, 'wb')
    pickle.dump(_pickle, file)


def convert(_data, fileName, method):
    if method == 'json':
        for i in tqdm(range(len(_data)), desc='Converting:'):
            dumpJson(fileName, _data)
    elif method == 'pickle':
        for i in tqdm(range(len(_data)), desc='Converting:'):
            dumpPickle(fileName, _data)
    else:
        return 'Error'


lines = loadFile('webcam.log')
for line in lines:
    stripped = line.split()
    time = stripped[4].split('.', 1)[0]
    data['occurrences'].append({'n_of_faces': stripped[1],
                               'time': time, 'date': stripped[3]})
convert(data, 'log.json', 'json')