
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#define SENSORPIN0 A0
#define SENSORPIN1 A1
#define SENSORPIN2 A2

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMSbot(0x60);
Adafruit_MotorShield AFMSmid(0x61);

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor7 = AFMSbot.getStepper(200, 1);
Adafruit_StepperMotor *myMotor8 = AFMSbot.getStepper(200, 2);
Adafruit_StepperMotor *myMotor9 = AFMSmid.getStepper(200, 2);

int sensorState = 0, lastState=0;  // variable for reading the pushbutton status

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  AFMSbot.begin();  // create with the default frequency 1.6KHz
  AFMSmid.begin();  // create with the default frequency 1.6KHz
  
  pinMode(SENSORPIN0,INPUT);
  digitalWrite(SENSORPIN0,HIGH);
  pinMode(SENSORPIN1,INPUT);
  digitalWrite(SENSORPIN1,HIGH);
  pinMode(SENSORPIN2,INPUT);
  digitalWrite(SENSORPIN2,HIGH);
}

void loop() {
  broken = 0
  if(Serial.available()){
    Serial.println("See pi");
    int i = Serial.parseInt();
    //Serial.println(turn);
    
    if(i == 7){
        while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN)
          myMotor7->step(1, FORWARD, SINGLE); 
          myMotor7->release();
          if(sensorState0==LOW){
            broken = 1
          }
         x++   
      }
    }
    if(i == 8){
      while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN1)
          myMotor8->step(1, FORWARD, SINGLE); 
          myMotor8->release();
          if(sensorState==LOW){
            broken = 1
          }
          else{
            broken = 0
          }
         x++ 
      }  
    }
    if(i == 9){
      while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN2)
          myMotor9->step(1, FORWARD, SINGLE); 
          myMotor9->release();
          if(sensorState==LOW){
            broken = 1
          }
          else{
            broken = 0
          }
         x++  
      }
    }
    Serial.flush(); 
  }
  lastState = sensorState;
}
