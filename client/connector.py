import serial
import json
import numpy as np

data_buff = []
recursion_track = 0
max_recursion = 100
deviceError = False

def connect_BTserial(port):
    ser = serial.Serial(port)
    print("Listening on port {}.".format(ser.name))
    return ser

def connect_USBserial(port, baudrate):
    ser = serial.Serial(port, baudrate)
    print("Listening on port {}.".format(ser.name))
    return ser

def get_from_serial(serial_obj):
    global data_buff, recursion_track, deviceError
    try:
        curr_line = serial_obj.readline()
        curr_str = curr_line.decode("utf-8").replace("\n", "").replace("\r", "")
        curr_data = json.loads(curr_str)
        data_buff.append(curr_data)
    except:
        recursion_track+=1
        if recursion_track < max_recursion:
            get_from_serial(serial_obj)
        else:
            deviceError=True
            print("ERROR: can't reach device or device messages are incomprehensible.")
            data_buff = None
        
def get_samples(serial_obj, num_lines):
    global data_buff
    data_buff = []
    for i in range(num_lines):
        get_from_serial(serial_obj)
    return data_buff