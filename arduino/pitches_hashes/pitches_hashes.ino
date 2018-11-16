/*
  LiquidCrystal Library - Cursor

 Demonstrates the use a 16x2 LCD display.  The LiquidCrystal
 library works with all LCD displays that are compatible with the
 Hitachi HD44780 driver. There are many of them out there, and you
 can usually tell them by the 16-pin interface.

 This sketch prints "Hello World!" to the LCD and
 uses the cursor()  and noCursor() methods to turn
 on and off the cursor.

 The circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)

 Library originally added 18 Apr 2008
 by David A. Mellis
 library modified 5 Jul 2009
 by Limor Fried (http://www.ladyada.net)
 example added 9 Jul 2009
 by Tom Igoe
 modified 22 Nov 2010
 by Tom Igoe
 modified 7 Nov 2016
 by Arturo Guadalupi

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/LiquidCrystalCursor

*/

// include the library code:
#include <LiquidCrystal.h>
#include "pitches.h"

//int sensorPin = A0;
//int sensorValue = 0;

int inInt;  // integer we will use for messages from the RPi

int Contrast = 20;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int zelda[] = {
  NOTE_E7, NOTE_F7, NOTE_FS7, NOTE_G7
};

int zelda_durations[] = {
  2,3,3,16
};


// music stuff
int melody[] = {
  NOTE_E7, NOTE_E7, 0, NOTE_E7,
  0, NOTE_C7, NOTE_E7, 0,
  NOTE_G7, 0, 0,  0,
  NOTE_G6, 0, 0, 0,

  NOTE_C7, 0, 0, NOTE_G6,
  0, 0, NOTE_E6, 0,
  0, NOTE_A6, 0, NOTE_B6,
  0, NOTE_AS6, NOTE_A6, 0,

  NOTE_G6, NOTE_E7, NOTE_G7,
  NOTE_A7, 0, NOTE_F7, NOTE_G7,
  0, NOTE_E7, 0, NOTE_C7,
  NOTE_D7, NOTE_B6, 0, 0,

  NOTE_C7, 0, 0, NOTE_G6,
  0, 0, NOTE_E6, 0,
  0, NOTE_A6, 0, NOTE_B6,
  0, NOTE_AS6, NOTE_A6, 0,

  NOTE_G6, NOTE_E7, NOTE_G7,
  NOTE_A7, 0, NOTE_F7, NOTE_G7,
  0, NOTE_E7, 0, NOTE_C7,
  NOTE_D7, NOTE_B6, 0, 0
};

int noteDurations[] = {
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
};

void trigger() {
 lcd.clear(); // clears the screen and buffer
 lcd.setCursor(0, 0); // set timer position on lcd for end.

 for (int positionCounter = 0; positionCounter < 16; positionCounter++) {
  // scroll one position left:
  lcd.setCursor(0, 1);
  lcd.scrollDisplayLeft();
  lcd.println("Making Money, Bitches....");
  // wait a bit:
  delay(500);
}
 
 int size = sizeof(melody) / sizeof(int);

 for (int thisNote = 0; thisNote < size; thisNote++) {

  // to calculate the note duration, take one second divided by the note type.
  //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
  int noteDuration = (1000 / noteDurations[thisNote]);
  tone(8, melody[thisNote], noteDuration);

  // to distinguish the notes, set a minimum time between them.
  // the note's duration + 30% seems to work well:
  int pauseBetweenNotes = noteDuration * 1.30;
  delay(pauseBetweenNotes);
  // stop the tone playing:
  noTone(8);
  }
 exit(0);
// delay(10000);

}

void setup() {
  Serial.begin(9600);

  analogWrite(6,Contrast);
  lcd.begin(16, 2);
  
//  // set up the LCD's number of columns and rows:
//  lcd.begin(16, 2);
  
  // Print a message to the LCD.
  lcd.print("Hashes! Bitches");
  lcd.setCursor(0, 2);
//  inInt = 666;
}

void loop() {
  
//  if(Serial.available()) {
//    inInt = (int)Serial.read();
//  }
  // print any value to the lcd display from serial
//  lcd.print(inInt);
//  if (inInt == 666) { 
//    trigger();
//  }
}