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
def main(_x,_y,fileName,outFileName):
    data = loadJson(fileName)
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
    plt.savefig(outFileName)
if(len(sys.argv) == 5):
    main(int(sys.argv[1]),int(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]))
else:
    print('wrong.')
