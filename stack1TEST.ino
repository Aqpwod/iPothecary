
#include <Wire.h>
#include <Adafruit_MotorShield.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMSbot(0x60);
Adafruit_MotorShield AFMSmid(0x61);

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor8 = AFMSbot.getStepper(200, 1);
Adafruit_StepperMotor *myMotor9 = AFMSbot.getStepper(200, 2);
Adafruit_StepperMotor *myMotor7 = AFMSmid.getStepper(200, 2);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);           // set up Serial library at 9600 bps
  AFMSbot.begin();  // create with the default frequency 1.6KHz
  AFMSmid.begin();  // create with the default frequency 1.6KHz
  
}

void loop() {
  // put your main code here, to run repeatedly:
   myMotor7->step(200, FORWARD, SINGLE); 
   myMotor7->release();
   myMotor8->step(200, FORWARD, SINGLE); 
   myMotor8->release();
   myMotor9->step(200, FORWARD, SINGLE); 
   myMotor9->release();

}
