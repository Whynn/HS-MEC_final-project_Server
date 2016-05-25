#include "./iolib.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define DUST_PORT 8
#define DUST_PIN 12   // P8_12
#define SAMPLETIME_MS 30000.0

double lowOccupancy = 0; // in ms
double fallingStart = 0; // in us

void edge_detected(int gpio, int level, double tick) {
    if(0 == level)
        fallingStart = tick;
    if(1 == level && fallingStart != 0)
        lowOccupancy += (tick - fallingStart) / 1000; //reduce resolution to ms
}

int main() {
    if(iolib_init() < 0) return 1; // init pigpio lib
    if(iolib_setdir(DUST_PORT, DUST_PIN, DIR_IN) < 0) return 1; // configure DUST_PIN as input
//    if(gpioSetAlertFunc(DUST_PIN, edge_detected) < 0) return 1; // configure interrupt routine for DUST_PIN
//    if(gpioDelay(SAMPLETIME_MS * 1000) < 0) return 1; // wait SAMPLETIME_MS (gpioDelay wants us)
//    gpioTerminate(); // try to terminate pigpio lib

    float ratio = (lowOccupancy / SAMPLETIME_MS) * 100; // calculate low occupancy in percent

  /*
  calculate particle concentration
  -> amount of particles per 283ml | particle size > 1um
  eqation for calculation from http://www.howmuchsnow.com/arduino/airquality/grovedust/
  */
    float concentration = 1.1 * ratio * ratio * ratio - 3.8 * ratio * ratio + 520 * ratio + 0.62;

  //printf("%d %f %f", lowOccupancy, ratio, concentration);
    printf("%.1f", ratio);
    return 0;
}