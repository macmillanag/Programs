#include <Servo.h>

Servo myservo;  //servo

int potpin = 0; //pot 
int val;   

void setup() {
  myservo.attach(9);  //  pin 9 to servo
}

void loop() {
  val = analogRead(potpin);            // reads potentiometer (value between 0 and 1023)
  val = map(val, 0, 1023, 0, 180);     // scale to use with servo between 0 and 180
  myservo.write(val);                  // sets servo position 
  delay(15);                           // waits 
}
