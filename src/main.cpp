#include "kernel/kernel.h"

Kernel kernel = Kernel();

void setup(){
    kernel.init();
}


void loop(){
    kernel.print_health();
}
