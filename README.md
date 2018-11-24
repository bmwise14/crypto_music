# CRYPTO MUSIC 

## TEAM
- Bradley Wise
- Rongxin Zhang

## 1) Initial Draft and Idea
- Our initial idea was to create a physical box that would create music by sending hashes as midi to a dj platform called Ableton Live. We had set up a miner on the raspberry pi that will be mining a type of cryptocurrency. The mining process would test many different hashes. The idea was to send a small number of these hash numbers to a python script which would be converted to readable midi notes by the computer and have them be displayed through arduino.
- Please see [ProjectDraft.md]() for more information.

## 2) Changes to Plan
- Much of the plan remains the same. However, we had some hurdles we had to go through that made us make slight changes to the overall project. The music being created from the hashes was less than stellar and really wasn't as cool as we thought it would be. Additionally, we were a little disappointed by the lack of interaction we were following. We realized we had to make some changes. We had to create some way for our physical device to be interactive than a stationary box that just output hash numbers and made terrible music. As Wendy Ju mentioned, we should try to make a self-contained device that does not rely on outside softwares.

## 4) Process
Part 1 - Backend
- a) Create a script that mines crypto currency over the raspberry pi
- b) create a python script that sends midi notes through a virtual port to Ableton Live
- c) Take the hashes and have them sent over as a json, which the python file can parse

Part 2 - Arduino
- a) Light Sensor - we wanted to use a light sensor
- b) LED Display -
- c) Lights - 
- d) Speakers - 
- e) Heart Rate Monitor - 

Part 3 - Physical Design
- a) Protoype 1: We first just wanted to design a physical box. We created a paper prototype that had a button, and LED Display, and a light. There was no functionality
- b) Prototype 2: Next we wanted to put our raspberry pi, arduino device, external battery, and speakers into 

## 3) Final Design and Code 
- Arduino
- Pi
- Sensors Used
    - Light Sensor
    - LED Display
    - 2 Lights
    - Heart Rate Monitor
- Final Design

