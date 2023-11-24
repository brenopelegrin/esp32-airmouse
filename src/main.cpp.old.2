#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

#include "pinout.h"

// Declarations for OTA

#include <WiFi.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

const char* ssid = "iot-network";
const char* password = "tio6!B8D*h(";

//#define USE_USB_SERIAL_INSTEAD_OF_BT_SERIAL

#ifdef USE_USB_SERIAL_INSTEAD_OF_BT_SERIAL
    #define SerialBT Serial
    #define BT_NAME 115200
#endif

#ifndef USE_USB_SERIAL_INSTEAD_OF_BT_SERIAL
    #include "BluetoothSerial.h"
    #define BT_NAME "esp32-airmouse"
    BluetoothSerial SerialBT;
#endif

// The class of Hall Effect Sensor

class Hall{
    private:
        static const int hallArraySize = HALL_ARRAY_SIZE;
        float hallValues[hallArraySize] = {0};
        const int hallPins[hallArraySize] = HALL_PINS;

    public:
        void initializeHallPins(){
            int i=0;
            for(i=0; i<hallArraySize; i++){
                pinMode(hallPins[i], INPUT);
            }   
        };

        void readAll(){
            int i=0;
            for(i=0; i<hallArraySize; i++){
                hallValues[i] = analogRead(hallPins[i]) * (3.158 / 4095.0);
            }
        };

        String getArrayAsString(){
            String Result = "[";

            int i=0;
            for(i=0; i<hallArraySize; i++){
                Result+= String(hallValues[i]);
                if(i < hallArraySize-1){
                    Result+=String(", ");
                }
            };

            Result+="]";
            return Result;
        };
};

bool blinkState = false;

String hallArrayAsString;

Hall myHall;

byte programState = 1;
byte flagOTA = 0;

Adafruit_MPU6050 mpu;

void setup() {
    myHall.initializeHallPins();
    SerialBT.begin(BT_NAME);

    if (!mpu.begin()) {
        SerialBT.println("[system] failed to find MPU6050 chip");
        programState = 100;
    }

    if(programState == 1){
        mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
        mpu.setGyroRange(MPU6050_RANGE_250_DEG);
        mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);
    }

    // configure LED for output
    pinMode(LED_PIN, OUTPUT);
    delay(10);
}

void setupOTA(){
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);

    while (WiFi.waitForConnectResult() != WL_CONNECTED) {
        delay(1000);
        ESP.restart();
    };

    // Port defaults to 3232
    // ArduinoOTA.setPort(3232);

    // Hostname defaults to esp3232-[MAC]
    // ArduinoOTA.setHostname("myesp32");

    // No authentication by default
    // ArduinoOTA.setPassword("admin");

    // Password can be set with it's md5 value as well
    // MD5(admin) = 21232f297a57a5a743894a0e4a801fc3
    // ArduinoOTA.setPasswordHash("21232f297a57a5a743894a0e4a801fc3");

    ArduinoOTA.onStart([]() {
        String type;
        if (ArduinoOTA.getCommand() == U_FLASH){
            type = "sketch";
        }
        else{ // U_SPIFFS
            type = "filesystem";
        }
        // NOTE: if updating SPIFFS this would be the place to unmount SPIFFS using SPIFFS.end()
        })
        .onEnd([]() {
        })
        .onProgress([](unsigned int progress, unsigned int total) {
        })
        .onError([](ota_error_t error) {
        if (error == OTA_AUTH_ERROR) SerialBT.println("Auth Failed");
        else if (error == OTA_BEGIN_ERROR) SerialBT.println("Begin Failed");
        else if (error == OTA_CONNECT_ERROR) SerialBT.println("Connect Failed");
        else if (error == OTA_RECEIVE_ERROR) SerialBT.println("Receive Failed");
        else if (error == OTA_END_ERROR) SerialBT.println("End Failed");
        });

    ArduinoOTA.begin();
}

void loop() {

    if(SerialBT.available() > 0){
        String instruction = SerialBT.readStringUntil('\n');
        if(instruction == String("stop_data")){
            programState = 0;
            SerialBT.println("[system] stop_data detected: stopping data fetching.");
        }

        if(instruction == String("start_data")){
            if(programState == 0){
                programState = 1;
                SerialBT.println("[system] start_data detected: starting data fetching.");
            }
            else{
                SerialBT.println("[system] start_data detected but data fetching isn't stopped.");
            }
        }

        if(instruction == String("start_ota")){
            programState = 2;
            SerialBT.println("[system] start_ota detected: stopping data fetching and starting OTA.");
        }
    }


    // State machine
    // 0 -> only wait for BT instructions
    // 1 -> fetch data and transmit to BT
    // 2 -> stop data fetch, start OTA update system
    // 3 -> OTA started, wait for instructions
    // 100 -> error

    if(programState == 100){
        SerialBT.println("[system] error");
        delay(10);
    }

    if(programState == 2){
        setupOTA();
        programState = 3;
    }

    if(programState == 3){
        ArduinoOTA.handle();
    }

    if(programState == 1){
        myHall.readAll();
        hallArrayAsString = myHall.getArrayAsString();

        sensors_event_t a, g, temp;
        mpu.getEvent(&a, &g, &temp);

        SerialBT.print("{");
        SerialBT.print("\"a\":[");
        SerialBT.print(a.acceleration.x);
        SerialBT.print(",");
        SerialBT.print(a.acceleration.y);
        SerialBT.print(",");
        SerialBT.print(a.acceleration.z);
        SerialBT.print("],");
        SerialBT.print("\"g\":[");
        SerialBT.print(g.gyro.x);
        SerialBT.print(",");
        SerialBT.print(g.gyro.y);
        SerialBT.print(",");
        SerialBT.print(g.gyro.z);
        SerialBT.print("],");

        SerialBT.print("\"temp\":[");
        SerialBT.print(temp.temperature);
        SerialBT.print("],");

        SerialBT.print("\"hall\":");
        SerialBT.print(hallArrayAsString);
        SerialBT.println("}");

        // blink LED to indicate activity
        blinkState = !blinkState;
        digitalWrite(LED_PIN, blinkState);
        
    }
}