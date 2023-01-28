from connector import *
import time
import json
port = "/dev/rfcomm0"
output_file = "output.json"
ser = connect_serial(port)

dataType = {
    "ypr": [],
    "a" : [],
    "g": [],
    "e": [],
    "ar": [],
    "aw": [],
    "q": [],
    "time": []
}

watch_time_in_seconds = 60*30
start_time = time.time()
current_time = 0
current_data = dataType
time_interval_in_seconds = 0.01

print("------------------")
print("Starting datalogger.\nWatch time (sec): {}\nTime interval (sec): {}\nOutput file: {}\n".format(watch_time_in_seconds, time_interval_in_seconds, output_file))

while current_time < watch_time_in_seconds and deviceError == False:
    current_time = time.time() - start_time
    current_data["time"].append(current_time)
    try:
        data_from_serial = get_samples(ser, 1)[0]
        for key in data_from_serial:
            if key in 
            current_data[key].append(data_from_serial[key])
    except:
        break
    time.sleep(time_interval_in_seconds)

with open(output_file, 'w') as file:
    print("Writing data to output file.")
    file.write(json.dumps(current_data))
print("Done.")
print("------------------")



