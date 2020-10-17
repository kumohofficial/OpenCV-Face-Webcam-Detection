import json
import sys
data = []
compressed_data = []
def loadJson(fileName):
    f = open(fileName,'r')
    data = json.load(f)
    return data
def dumpJson(fileName, _json):
    file = open(fileName, 'w')
    json.dump(_json, file, indent=4, sort_keys=True)
def compress(every_minute,_data):
    temp = 0
    faces = 0

    for occurrence in _data:
        data.append({
            'n_of_faces': occurrence['n_of_faces'],
            'time': occurrence['time']
            })
        faces += int(occurrence['n_of_faces'])
        if(not temp % (every_minute-1) and not temp == 0):
            compressed_data.append({
                'n_of_faces': faces,
                'time': occurrence['time']
                })
            faces = 0
        temp += 1
def main(every_minute):
    jsonData = loadJson('log.json')
    print("Compressing Faces of {} length by {}.".format(len(jsonData),every_minute))
    compress(every_minute,jsonData)
    dumpJson('compressed.json',compressed_data)
    print('Final number of entries:{}'.format(len(compressed_data)))
if(len(sys.argv) == 2):
    main(int(sys.argv[1]))
else:
    print("Specify every_minute.")
    print(len(sys.argv))
