import matplotlib.pyplot as plt
import json
import sys
def loadJson(fileName):
    f = open(fileName,'r')
    data = json.load(f)
    return data
def showGraph(x_arr,y_arr):
    plt.plot(x_arr,y_arr)
    plt.xlabel('Number of face occurrences')
    plt.xlabel('Time')
    plt.title('Faces')
    plt.show()
def main(_x,_y):
    data = loadJson('compressed.json')
    time = []
    faces = []
    for index in data:
        time.append(index['time'])
        faces.append(index['n_of_faces'])
    plt.rcParams['agg.path.chunksize'] = 200000
    plt.rcParams['figure.figsize'] = (_x,_y)
    figure,ax = plt.subplots()
    ax.plot_date(time,faces,marker='',linestyle='-')
    figure.autofmt_xdate()
    #plt.show()
    plt.savefig('main.png')

if(len(sys.argv) == 3):
    main(sys.argv[1],sys.argv[2])
else:
    print('wrong.')
