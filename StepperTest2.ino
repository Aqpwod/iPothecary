#include <Wire.h>
#include <Adafruit_MotorShield.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMSbot(0x60);
Adafruit_MotorShield AFMSmid(0x61);
Adafruit_MotorShield AFMStop(0x62);
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor1 = AFMSbot.getStepper(200, 1);
Adafruit_StepperMotor *myMotor2 = AFMSmid.getStepper(200, 2);
Adafruit_StepperMotor *myMotor3 = AFMStop.getStepper(200, 1);


void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test!");

  AFMSbot.begin();  // create with the default frequency 1.6KHz
  AFMSmid.begin();  // create with the default frequency 1.6KHz
  AFMStop.begin();  // create with the default frequency 1.6KHz

  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
}

void loop() {
  if(Serial.available()){
    Serial.println("See pi");
    int i = Serial.parseInt();

    Serial.println(i);
    //Serial.println(turn);
    
    if(i == 1){
      myMotor1->step(200, FORWARD, SINGLE); 
      myMotor1->release();
    }
    if(i == 2){
      myMotor2->step(200, FORWARD, SINGLE); 
      myMotor2->release();
    }
    if(i == 3){
      myMotor3->step(200, FORWARD, SINGLE); 
      myMotor3->release();
    }
    if(i == 4){
      myMotor1->step(100, FORWARD, SINGLE); 
      myMotor1->release();
    }
    if(i == 5){
      myMotor2->step(100, FORWARD, SINGLE); 
      myMotor2->release();
    }
    if(i == 6){
      myMotor3->step(100, FORWARD, SINGLE); 
      myMotor3->release();
    }
    
    
    Serial.flush(); 
  }
}
