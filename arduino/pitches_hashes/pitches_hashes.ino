/*
 http://www.arduino.cc/en/Tutorial/LiquidCrystalCursor
*/

// include the library code:
#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library. 
#include <LiquidCrystal.h>
#include "pitches.h"

//  Variables
const int PulseWire = A2;       // PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED13 = 13;          // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;           // Determine which Signal to "count as a beat" and which to ignore.
                               // Use the "Gettting Started Project" to fine-tune Threshold Value beyond default setting.
                               // Otherwise leave the default "550" value. 

int inInt;  // integer we will use for messages from the RPi

int onPin = 9;
int alertPin = 10;
int Contrast = 20;
int lightSensorPin = A0;
int analogValue = 0;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

PulseSensorPlayground pulseSensor;  // Creates an instance of the PulseSensorPlayground object called "pulseSensor"



int zelda[] = {
  NOTE_E7, NOTE_F7, NOTE_FS7, NOTE_G7
};

int zelda_durations[] = {
  4,4,4,16
};

void trigger() {
 lcd.clear(); // clears the screen and buffer
 lcd.setCursor(0, 0); // set timer position on lcd for end.

 for (int positionCounter = 0; positionCounter < 16; positionCounter++) {
  // scroll one position left:
  lcd.setCursor(0, 1);
//  lcd.scrollDisplayLeft();
  lcd.println("Making Money");
  // wait a bit:
}
 
 int size = sizeof(zelda) / sizeof(int);

 for (int thisNote = 0; thisNote < size; thisNote++) {

  // to calculate the note duration, take one second divided by the note type.
  //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
  int zelda_duration = (1000 / zelda_durations[thisNote]);
  tone(8, zelda[thisNote], zelda_duration);

  // to distinguish the notes, set a minimum time between them.
  // the note's duration + 30% seems to work well:
  int pauseBetweenNotes = zelda_duration * 1.30;
  delay(pauseBetweenNotes);
  // stop the tone playing:
  noTone(8);
  }
// exit(0);
// delay(10000);

}

void setup() {
  Serial.begin(9600);
  
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       //auto-magically blink Arduino's LED with heartbeat.
  pulseSensor.setThreshold(Threshold);   

  if (pulseSensor.begin()) {
    Serial.println("We created a pulseSensor Object !");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  }

  analogWrite(6,Contrast);
  lcd.begin(16, 2);
  
  // Print a message to the LCD.
  lcd.print("Hashes!");
  pinMode(onPin, OUTPUT);
  pinMode(alertPin, OUTPUT);
}

void loop() {
  
  analogValue = analogRead(lightSensorPin);
  int myBPM = pulseSensor.getBeatsPerMinute();  // Calls function on our pulseSensor object that returns BPM as an "int".
                                               // "myBPM" hold this BPM value now. 

//    if (pulseSensor.sawStartOfBeat()) {            // Constantly test to see if "a beat happened". 
// Serial.println("♥  A HeartBeat Happened ! "); // If test is "true", print a message "a heartbeat happened".
// Serial.print("BPM: ");                        // Print phrase "BPM: " 
// Serial.println(myBPM);                        // Print the value inside of myBPM. 
//}

  if (analogValue > 800 and pulseSensor.sawStartOfBeat()) {
    Serial.println("turn_on");
    pulseSensor.blinkOnPulse(onPin);
//    digitalWrite(onPin, HIGH);
    
    String hash = readSerial();
    if (hash.indexOf("found_hash")>-1) {
      digitalWrite(alertPin, HIGH);
//      digitalWrite(onPin, LOW);
      trigger();
      digitalWrite(alertPin, LOW);
    }


    Serial.println(hash);
    
    lcd.print(myBPM);
    lcd.setCursor(3, 1);
    
    lcd.print(hash);
    
    delay(500);
    lcd.clear();
  }
  
  else {
    Serial.println("turn_off");
    digitalWrite(onPin, LOW);

  }

  
}

// Read string from serial
String readSerial(){
  char incomingByte = 0;  // for incoming serial data
  String readString = "";
  
  // reply only when you receive data:
  while (Serial.available()) {
    // read the incoming byte:
    incomingByte = Serial.read();
    readString += incomingByte;
   
  }
  if (Serial.available() == 0){
    Serial.flush();
    return readString;
  }
}
