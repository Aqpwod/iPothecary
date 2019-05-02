
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#define SENSORPIN0 A0
#define SENSORPIN1 A1
#define SENSORPIN2 A2
#define SENSORPIN3 A3
#define SENSORPIN4 A4
#define SENSORPIN5 A5

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMSbot(0x60);
Adafruit_MotorShield AFMSmid(0x61);
Adafruit_MotorShield AFMStop(0x62);

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor1 = AFMSbot.getStepper(200, 1);
Adafruit_StepperMotor *myMotor2 = AFMSbot.getStepper(200, 2);
Adafruit_StepperMotor *myMotor3 = AFMSmid.getStepper(200, 1);
Adafruit_StepperMotor *myMotor4 = AFMSmid.getStepper(200, 2);
Adafruit_StepperMotor *myMotor5 = AFMStop.getStepper(200, 1);
Adafruit_StepperMotor *myMotor6 = AFMStop.getStepper(200, 2);

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
  pinMode(SENSORPIN3,INPUT);
  digitalWrite(SENSORPIN3,HIGH);
  pinMode(SENSORPIN4,INPUT);
  digitalWrite(SENSORPIN4,HIGH);
  pinMode(SENSORPIN5,INPUT);
  digitalWrite(SENSORPIN5,HIGH);
  
}

void loop() {
  broken = 0
  if(Serial.available()){
    Serial.println("See pi");
    int i = Serial.parseInt();
    //Serial.println(turn);
    
    if(i == 1){
        while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN0)
          myMotor1->step(1, FORWARD, SINGLE); 
          myMotor1->release();
          if(sensorState0==LOW){
            broken = 1
          }
         x++   
      }
    }
    if(i == 2){
      while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN1)
          myMotor2->step(1, FORWARD, SINGLE); 
          myMotor2->release();
          if(sensorState==LOW){
            broken = 1
          }
          else{
            broken = 0
          }
         x++ 
      }  
    }
    if(i == 3){
      while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN2)
          myMotor3->step(1, FORWARD, SINGLE); 
          myMotor3->release();
          if(sensorState==LOW){
            broken = 1
          }
          else{
            broken = 0
          }
         x++  
      }
    }
    if(i == 4){
        while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN3)
          myMotor4->step(1, FORWARD, SINGLE); 
          myMotor4->release();
          if(sensorState0==LOW){
            broken = 1
          }
         x++   
      }
    }
    if(i == 5){
      while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN4)
          myMotor5->step(1, FORWARD, SINGLE); 
          myMotor5->release();
          if(sensorState==LOW){
            broken = 1
          }
          else{
            broken = 0
          }
         x++ 
      }  
    }
    if(i == 6){
      while(x<200 && broken==0){
          sensorState = digitalRead(SENSORPIN5)
          myMotor6->step(1, FORWARD, SINGLE); 
          myMotor6->release();
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
