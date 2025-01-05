#include <Servo.h>
#include <Ultrasonic.h>

Servo servo;
int trig = 9; 
int echo = 10;
int dist;
int duration;
int angle = 0;
bool counterClockwise = true;

// Upload this code onto your microcontroller and run the python app, make sure the IDE's serial monitor is not open    

int readSonic() {
  digitalWrite(trig, 0); //clear the trigger for 2 microseconds
  delayMicroseconds(2);
  digitalWrite(trig, 1); //send out ultrasound waves for 10 microseconds
  delayMicroseconds(10);
  duration = pulseIn(echo, 1); //recieve the duration of te ultrasound wave
  dist = duration * 0.034/2; //calculates the distance from pinged object
  if (dist>60) {
    dist = 60;
  }
  return dist;
}

void updateServo() {
  //checks the direction of rotation, counterclockwise is true at the start, and increments/decrements accordingly
  if (counterClockwise) {
    angle++;
  }
  else {
    angle--;
  }
  //if the servo reaches the min or max, change the direction of rotation
  if (angle<=0) {
    counterClockwise = true;
  }
  else if (angle >= 180) {
    counterClockwise = false;
  }
  //set the servo's angle
  servo.write(angle);
}
void setup() {
  servo.attach(3); //init servo
  servo.write(angle); //set servo to starting pos
  pinMode(trig, OUTPUT); //init trig
  pinMode(echo, INPUT); //init echo
  Serial.begin(9600); //init serial comms
  delay(1000); //starting delay
}

void loop() {
  updateServo(); //updates the servo's position by one degree and waits for 75 miliseconds
  delay(150);
  Serial.print(readSonic()); //print the distance of pinged target to serial port
  Serial.print(" ");
  Serial.println(angle);
  //The code below is very specific to my servo, I was encountering an odd problem where the servo traveled in the wrong direction, if this is happening for you, uncomment the line below and comment out the one above
  //Serial.println(abs(angle-180));
}
