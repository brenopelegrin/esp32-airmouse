#include "kernel/kernel.h"

class SerialComm{
    private:
        short unsigned int serial_type = 0;

    public:
        // constructor
        SerialComm(short unsigned int type){
            serial_type = type;
        };

        // destructor
        ~SerialComm(){
            switch(serial_type){
                case 0:
                    break;
                case 1:
                    // implement BT serial destroy
                    break;
                default:
                    break;
            }
        }

        void println(char* msg){
            switch(serial_type){
                case 0:
                    Serial.println(msg);
                    break;
                case 1:
                    // implement BT serial
                    break;
                default:
                    break;
            }
            return;
        };
        void print(char* msg){
            switch(serial_type){
                case 0:
                    Serial.print(msg);
                    break;
                case 1:
                    // implement BT serial
                    break;
                default:
                    break;
            }
            return;
        };
};

class Kernel{
    public:
        Kernel();
        SerialComm comm = SerialComm(0);
        short unsigned int init(){
            comm.println("[kernel] starting kernel");
            return 1;
        };
        void print_health(){
            comm.println("[kernel] health check");
            return;
        }
};