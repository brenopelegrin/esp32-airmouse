from connector import *
import time
import json
import os.path
port = "/dev/rfcomm0"
output_file = "outputs/output.json"
ser = connect_BTserial(port)

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

watch_time_in_seconds = 5
start_time = time.time()
current_time = 0
current_data = dataType
time_interval_in_seconds = 0.01

print("------------------")
print(f"Starting datalogger.\nWatch time (sec): {watch_time_in_seconds}\nTime interval (sec): {time_interval_in_seconds}\nOutput file: {output_file}\n")

# Still needs to implement some form of saving the current state to the json file
# to prevent exceeding memory capacity and avoid eventual data losses

while current_time - start_time < watch_time_in_seconds and deviceError == False:
    current_time = time.time()
    current_data["time"].append(current_time)
    try:
        data_from_serial = get_samples(ser, 1)[0]
        print(data_from_serial)
        for key in data_from_serial:
            current_data[key].append(data_from_serial[key])
    except:
        break
    time.sleep(time_interval_in_seconds)

count_file = 1
while os.path.exists(output_file):
    print(f'File {output_file} already exists.')
    output_file = output_file+'.'+str(count_file)
    count_file+=1
    print(f'Trying new output file: {output_file}\n')
    
with open(output_file, 'w') as file:
    print(f'Writing data to output file {output_file}.')
    file.write(json.dumps(current_data))
print("Done.")
print("------------------")



