#include <Arduino.h>

class SerialComm{
    private:
        short unsigned int serial_type = 0;

    public:
        // constructor
        SerialComm(short unsigned int type);

        // destructor
        ~SerialComm();

        void println(char* msg);
        void print(char* msg);
};

class Kernel{
    public:
        short unsigned int init();
        void print_health();
};