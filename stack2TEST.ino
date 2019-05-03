
#include <Wire.h>
#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMSbot(0x60);
Adafruit_MotorShield AFMSmid(0x61);
Adafruit_MotorShield AFMStop(0x62);
Adafruit_StepperMotor *myMotor5 = AFMSbot.getStepper(200, 1);
Adafruit_StepperMotor *myMotor6 = AFMSbot.getStepper(200, 2);
Adafruit_StepperMotor *myMotor3 = AFMSmid.getStepper(200, 1);
Adafruit_StepperMotor *myMotor4 = AFMSmid.getStepper(200, 2);
Adafruit_StepperMotor *myMotor2 = AFMStop.getStepper(200, 1);
Adafruit_StepperMotor *myMotor1 = AFMStop.getStepper(200, 2);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);           // set up Serial library at 9600 bps
  AFMSbot.begin();  // create with the default frequency 1.6KHz
  AFMSmid.begin();  // create with the default frequency 1.6KHz
  AFMStop.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
   myMotor1->step(200, FORWARD, SINGLE); 
   myMotor1->release();
   myMotor2->step(200, FORWARD, SINGLE); 
   myMotor2->release();
   myMotor3->step(200, FORWARD, SINGLE); 
   myMotor3->release();
   myMotor4->step(200, FORWARD, SINGLE); 
   myMotor4->release();
   myMotor5->step(200, FORWARD, SINGLE); 
   myMotor5->release();
   myMotor6->step(200, FORWARD, SINGLE); 
   myMotor6->release();
   
}
