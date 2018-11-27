# CRYPTO MUSIC 

## TEAM
- Bradley Wise
- Rongxin Zhang

## 1) Initial Draft and Idea
- Our initial idea was to create a physical box that would create music by sending hashes as midi to a dj platform called Ableton Live. We had set up a miner on the raspberry pi that will be mining a type of cryptocurrency. The mining process would test many different hashes. The idea was to send a small number of these hash numbers to a python script which would be converted to readable midi notes by the computer and have them be displayed through arduino.
- Please see [ProjectDraft.md](https://github.com/bmwise14/crypto_music/blob/master/ProjectDraft.md) for more information.

## 2) Changes to Plan
- Much of the plan remains the same. However, we had some hurdles we had to go through that made us make slight changes to the overall project. The music being created from the hashes was less than stellar and really wasn't as cool as we thought it would be. Additionally, we were a little disappointed by the lack of interaction. We realized we had to make some changes. 

- We wanted to create some way for our physical device to be interactive than a stationary box that just output hash numbers and made terrible music. As Wendy Ju mentioned, we should try to make a self-contained device that does not rely on outside softwares. So, we added a heart rate monitor, light sensors, and a speaker to create a more self-contained interactive device. The outline for our process in building in these components is below.

## 4) Process
**Part 1 - Backend**
- a) Create a script that mines crypto currency over the raspberry pi
- b) create a python script that sends midi notes by a virtual port to Ableton Live (may not be used in final project).
- c) Take the hashes and have them sent over as a json, which the python file can parse and sent do Ableton as midi to make music.

**Part 2 - Arduino**
- a) Light Sensor - we wanted to use a light sensor to turn on and off our crypto-miner. Crypto Box only works during the day.
- b) Heart Rate Monitor - This is will be connected to your finger and will serve as a link to you and the crypto box. The crypto miner's pulse is tied to yours, such that it is only works when you have a pulse.
- c) LCD Display - The display is used to output your heart rate and show the hashes being mined. It will also display different messages after a successful mine.
- d) Lights - we have a blue light to signal when a coin has been successfully mined. The red light will chime on and off according to your heart rate. You and the crypto-box will be biologically linked. It only works when you have a pulse.
- e) Speakers - The speakers will sound a success tone every time a coin has been mined successfully.
- [Arduino Code](https://github.com/bmwise14/crypto_music/blob/master/arduino/pitches_hashes/pitches_hashes.ino)

**Part 3 - Physical Design**
- a) Protoype 1: We first just wanted to design a physical box. We created a paper prototype that had a button, and LED Display, and a light. There was no functionality whatsoever and is highlighted in our first draft [here](https://github.com/bmwise14/crypto_music/blob/master/ProjectDraft.md).
- b) Prototype 2: Next we wanted to put our raspberry pi, arduino device, external battery, and speakers into a physical box-like object that gives a more sleek and refined look. Here is the new [box -NEED IMAGE HERE]().
- c) Prototype 3: 

## 3) Final Design and Code 
- Arduino
- Pi
- Sensors Used
    - Light Sensor
    - LED Display
    - 2 Lights
    - Heart Rate Monitor
- Final Design

