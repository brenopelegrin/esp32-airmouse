import numpy as np
from connector import *

datalistSlice = 60

def animate_3line(i, ax, dataList, ser, line):
    atual = np.array(get_samples(ser, 1)[0][line])
    dataList.append([atual[0], atual[1], atual[2]])
    
    dataList = dataList[-datalistSlice:]
    dataList_arr = np.array(dataList)
    
    ax.clear()
    ax.plot(dataList_arr[:,0], label="x")
    ax.plot(dataList_arr[:,1], label="y")
    ax.plot(dataList_arr[:,2], label="z")
    ax.set_title(line)
    ax.set_ylabel("")
    ax.grid()
    ax.legend()

def animate_5line(i, ax, dataList, ser, line):
    atual = np.array(get_samples(ser, 1)[0][line])
    dataList.append([atual[0], atual[1], atual[2], atual[3], atual[4]])
    
    dataList = dataList[-datalistSlice:]
    dataList_arr = np.array(dataList)
    
    ax.clear()
    ax.plot(dataList_arr[:,0], label="0")   
    ax.plot(dataList_arr[:,1], label="1")
    ax.plot(dataList_arr[:,2], label="2")
    ax.plot(dataList_arr[:,3], label="3")
    ax.plot(dataList_arr[:,4], label="4")
    ax.set_title(line)
    ax.set_ylabel("")
    ax.grid()
    ax.legend()

def animate_1line(i, ax, dataList, ser, line):
    atual = np.array(get_samples(ser, 1)[0][line])
    dataList.append(atual)
    
    dataList = dataList[-datalistSlice:]
    dataList_arr = np.array(dataList)
    
    ax.clear()
    ax.plot(dataList_arr, label="x")
    ax.set_title(line)
    ax.set_ylabel("")
    ax.grid()
    ax.legend()

def animate_4line(i, ax, dataList, ser, line):
    atual = np.array(get_samples(ser, 1)[0][line])
    dataList.append([atual[0], atual[1], atual[2], atual[3]])
    
    dataList = dataList[-datalistSlice:]
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