### client
Here, there is the source code for the pc-side client that will listen to ESP32 data on Bluetooth, plot graphics, log data and convert data into movement.

First, clone the repository, create a virtual environment and install the dependencies:
```bash
cd esp32-airmouse/client &&
python -m venv ./ &&
source ./bin/activate &&
pip install -r ./requirements.txt
```

Before running any script of the client-side, if you are going to use Bluetooth, you need to bind the ESP32 MAC Address in the rfcomm0. For example, for an ESP32 with mac address ``24:0A:C4:EE:A3:32``, you should run:

```bash
sudo rfcomm bind 0 24:0A:C4:EE:A3:32 1
```

#### **datalogger.py**
This script listens to the ESP32 on bluetooth or other serial and logs the data into files.
You can customize the variables in the code:

```python
watch_time_in_seconds = 5 # How many seconds do you want to run
time_interval_in_seconds = 0.01 # How many seconds you want to wait between each measurement

```

After configuring, run the script:
```bash
python datalogger.py
```

#### **monitor.py**
This script listens to the ESP32 on bluetooth or other serial and print the output on terminal.
You can customize the variables in the code:

```python
time_interval_in_seconds = 0.01 # How many seconds you want to wait between each measurement

```

After configuring, run the script:
```bash
python monitor.py
```

#### **animator.py**
This script listens to the ESP32 on bluetooth or other serial and plot some graphics about the data.

To run the script, do:
```bash
python animated_plotter.py
```
