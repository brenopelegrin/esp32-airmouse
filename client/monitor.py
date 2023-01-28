from connector import *
import time
import json
import os.path
port = "/dev/rfcomm0"
ser = connect_serial(port)

dataType = {
    "ypr": [],
    "a" : [],
    "g": [],
    "e": [],
    "ar": [],
    "aw": [],
    "q": [],
    "time": [],
    "hall": []
}

current_data = dataType
time_interval_in_seconds = 0.001

print("------------------")
print(f"Starting monitor.\nTime interval (sec): {time_interval_in_seconds}\n")

while True:
    try:
        data_from_serial = get_samples(ser, 1)[0]
        print(data_from_serial)
    except:
        break
    time.sleep(time_interval_in_seconds)



