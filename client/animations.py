import numpy as np
from connector import *

def animate_3line(i, ax, dataList, ser, line):
    atual = np.array(get_samples(ser, 1)[0][line])
    dataList.append([atual[0], atual[1], atual[2]])
    
    dataList = dataList[-50:]
    dataList_arr = np.array(dataList)
    
    ax.clear()
    ax.plot(dataList_arr[:,0], label="x")
    ax.plot(dataList_arr[:,1], label="y")
    ax.plot(dataList_arr[:,2], label="z")
    ax.set_title(line)
    ax.set_ylabel("")
    ax.grid()
    ax.legend()

def animate_4line(i, ax, dataList, ser, line):
    atual = np.array(get_samples(ser, 1)[0][line])
    dataList.append([atual[0], atual[1], atual[2], atual[3]])
    
    dataList = dataList[-50:]
    dataList_arr = np.array(dataList)
    
    ax.clear()
    ax.plot(dataList_arr[:,0], label="x")
    ax.plot(dataList_arr[:,1], label="y")
    ax.plot(dataList_arr[:,2], label="z")
    ax.plot(dataList_arr[:,3], label="w")
    ax.set_title(line)
    ax.set_ylabel("")
    ax.grid()
    ax.legend()