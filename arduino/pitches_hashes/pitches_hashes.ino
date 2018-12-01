// include the library code:
#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library. 
#include <LiquidCrystal.h>
#include "pitches.h"

//  Variables
const int PulseWire = A2;       // PulseSensor PURPLE WIRE

int Threshold = 450; // Pulse Threshold

int Contrast = 20; // Scren contracts

int inInt;  // integer we will use for messages from the RPi

int onPin = 9; // Blue
int alertPin = 10; // RED 

const int LIGHT_ON_THRESHOLD = 800;

int lightSensorPin = A0; // Light sensor
int sensorValue = 0;

bool isOff = true;

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

/*
 * When we find a hash
 */
void trigger() {
  
  lcd.clear(); // clears the screen and buffer
  lcd.setCursor(0, 0); // set timer position on lcd for end.

  for (int positionCounter = 0; positionCounter < 16; positionCounter++) {
    // scroll one position left:
    lcd.setCursor(0, 0);
    lcd.print("**Making Money**");
  }
  
  playMusic();
  
}

/*
 * Play Zelda Music
 */
void playMusic(){
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
}


unsigned long oldTime;
unsigned long newTime;

void setup() {
  
  Serial.begin(9600);
  randomSeed(analogRead(0));

  oldTime = millis();
  
  // 
  pinMode(onPin, OUTPUT); // Blue light
  pinMode(alertPin, OUTPUT); //
  
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.setThreshold(Threshold);   

  if (pulseSensor.begin()) {
    Serial.println("We created a pulseSensor Object !");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  }

  analogWrite(6,Contrast);
  
  lcd.begin(16, 2);
  
  // Print a message to the LCD.
  lcd.print("We are started");
 
  
}


void loop() {

  // Light sensor value
  sensorValue = analogRead(lightSensorPin);

  newTime = millis();
  
  int myBPM = pulseSensor.getBeatsPerMinute();  // Calls function on our pulseSensor object that returns BPM as an "int".
                                               
  if (pulseSensor.sawStartOfBeat()) {            
   Serial.println(myBPM);                        
  }

  if (sensorValue < LIGHT_ON_THRESHOLD and myBPM > 50 and myBPM < 120) {
    // Notification to turn on Miner
    Serial.println("turn_on");

    isOff = false;
    
    pulseSensor.blinkOnPulse(onPin);

    String hash = readSerial();
//    String hash = testHashes();  
//    
    if (hash.indexOf("found_hash") > -1) {
      digitalWrite(alertPin, HIGH);
      delay(500);
      digitalWrite(alertPin, LOW);
      trigger();
    }

    Serial.println(hash);
    
    pulseSensor.blinkOnPulse(onPin);
    
    lcd.print("BPM:  " + String(myBPM));

    //  
    lcd.setCursor(0, 1);
    lcd.print("Hash: " + hash);
//    digitalWrite(onPin, HIGH);
    
//    Serial.println(hash);
    delay(500); 
    
  } else {
    if (newTime - oldTime > 5000){
      if (!isOff){
        Serial.println("turn_off");  
      }
      Serial.println("in timer");  
      oldTime = newTime;
    }
    
    isOff = true;
    
    digitalWrite(onPin, LOW);
    
    lcd.print("We are off...");
  }

  lcd.clear();
}

String testHashes(){
  int randNumber = random(100);
  
  delay(300);
  
  if (randNumber < 5){
    return "found_hash";
  } else {
    return "23984572345";
  };
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
