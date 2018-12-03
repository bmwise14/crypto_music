# CRYPTO MUSIC MINOR

#### TEAM
- Bradley Wise (bmw246)
- Rongxin Zhang (rz345)

## Initial Draft and Idea
![img_3555](https://user-images.githubusercontent.com/3782456/49352254-059c1b00-f685-11e8-91cd-5b47ff73a587.jpeg)
Our initial idea was to create a physical box that would create music by sending hashes as midi to a dj platform called Ableton Live. We had set up a miner on the raspberry pi that will be mining a type of cryptocurrency. The mining process would test many different hashes. The idea was to send a small number of these hash numbers to a python script which would be converted to readable midi notes by the computer and have them be displayed through arduino. Please see [ProjectDraft.md](ProjectDraft.md) for more information.

## Changes to Plan
Much of the plan remains the same. However, we had some hurdles we had to go through that made us make slight changes to the overall project. The music being created from the hashes was less than stellar and really wasn't as cool as we thought it would be. Additionally, we were a little disappointed by the lack of interaction. We realized we had to make some changes. 

We wanted to create some way for our physical device to be interactive than a stationary box that just output hash numbers and made terrible music. As Wendy Ju mentioned, we should try to make a self-contained device that does not rely on outside softwares. So, we added a heart rate monitor, light sensors, and a speaker to create a more self-contained interactive device. The outline for our process in building in these components is below.

## Componenets
### Raphasberry Pi Server

a) Create a script that mines crypto currency over the raspberry pi

We leveraged: https://github.com/tpruvot/cpuminer-multi core code, and added additional changes to the code, such that it can communicate with the Arduino over serial ports. Please see the [customized code](./miner/qubit.c) for more information.
  
b) Create a python script that sends midi notes by a virtual port to Ableton Live (may not be used in final project). Please refer to [crypto_music.py](https://github.com/bmwise14/crypto_music/blob/master/crypto_midi/crypto_music.py) in the [crypto midi](https://github.com/bmwise14/crypto_music/tree/master/crypto_midi) folder.

c) Send information to Arduino over serial and post them over HTTP to another python server which interacts with Ableton as midi to make music.


### Arduino
![img_3508](https://user-images.githubusercontent.com/3782456/49352379-9f63c800-f685-11e8-977a-3b825ce01def.jpeg)

** Devices Used:** Rhasberry Pi, Arduino, Light Sensor, LED Display, 2 Lights, Heart Rate Monitor

a) Light Sensor - we wanted to use a light sensor to turn on and off our crypto-miner. Crypto Box only works during the day.

b) Heart Rate Monitor - This is will be connected to your finger and will serve as a link to you and the crypto box. The crypto miner's pulse is tied to yours, such that it is only works when you have a pulse. The Heart Rate Monitor was based off the [PulseSensor project](https://pulsesensor.com/pages/code-and-guide). We tied the [PulseSensor_BPM](https://pulsesensor.com/pages/getting-advanced) code in arduino to our own arduino code.

c) LCD Display - The display is used to output your heart rate and show the hashes being mined. It will also display different messages after a successful mine. Here is the [video](https://www.youtube.com/watch?v=zzGWcZ2E5CY) we used to connect the LCD display without a potentiometer.

d) Lights - we have a blue light to signal when a coin has been successfully mined. The red light will chime on and off according to your heart rate. You and the crypto-box will be biologically linked. It only works when you have a pulse.

e) Speakers - The speakers will sound a success tone every time a coin has been mined successfully. Attached is the full [Arduino Code](./pitches_hashes/pitches_hashes.ino)

e) Power Pack - Since we wanted this item to be competely portable, we added a large power pack that could power the entire operation.

#### Demo Video:
When we were just testing the internal items

[![](https://img.youtube.com/vi/MJOnnCxagro/0.jpg)](https://youtu.be/MJOnnCxagro) 

### Physical Design:
![screen shot 2018-12-02 at 11 21 46 pm](https://user-images.githubusercontent.com/3782456/49352960-12bb0900-f689-11e8-84c3-3f36eef3b9f0.png)

We went through multiple iterations to get the correct shape, and design. We mainly used the lazer cutter to create the required shapes for the box. SpecificallWe also used glue guns to join the sections. The full illustrator file can be found  
[here](./crypto-box-new-final.ai)


## Final Product

![img_3677](https://user-images.githubusercontent.com/3782456/49352722-6e849280-f687-11e8-8579-0362b00a6960.jpeg)

The idea with the Crypto Music Minor is that you have to caress it. You must hold it with two hands and cuddle it with your heart before it will start mining cryptocurrencies for you. The below video will show how this works.

![screen shot 2018-12-02 at 11 06 44 pm](https://user-images.githubusercontent.com/3782456/49352676-21082580-f687-11e8-8685-69f1182267fa.png)

These are the various angles of the miner. We took Andrea's advice to make the sides using clear acrylic as well as to make the light section flush.

##### Demo Video
[![](https://img.youtube.com/vi/m1Q9HMr6kQ0/0.jpg)](https://youtu.be/m1Q9HMr6kQ0) 


## Prototyping Process:

We developed multiple prototypes to test the functionality and design of the Crypto Music Minor.

##### a) Protoype 1:
![screen shot 2018-12-02 at 10 56 18 pm](https://user-images.githubusercontent.com/3782456/49352461-01bcc880-f686-11e8-8513-6e70fb316f6b.png)
We first just wanted to design a physical box. We created a paper prototype that had a button, and LED Display, and a light. There was no functionality whatsoever and is highlighted in our first draft [here]

##### b) Prototype 2:
![screen shot 2018-12-02 at 10 59 47 pm](https://user-images.githubusercontent.com/3782456/49352462-01bcc880-f686-11e8-87be-2ce953fed96c.png)
Next we wanted to put our raspberry pi, arduino device, external  battery, and speakers into a physical box-like object that gives a friendlier look.
##### Demo Video
[![](https://img.youtube.com/vi/F3bVqpSFKPQ/0.jpg)](https://youtu.be/F3bVqpSFKPQ)



##### c) Prototype 3:
We perforated holes at the seams to create the design. Here is our Illustrator ![screen shot 2018-12-02 at 11 03 07 pm](https://user-images.githubusercontent.com/3782456/49352555-73951200-f686-11e8-8301-878870b86623.png)

##### Demo Video
[![](https://img.youtube.com/vi/VrxEEp9DG1w/0.jpg)](https://youtu.be/VrxEEp9DG1w) 
