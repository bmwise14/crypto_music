import mido
import time
import random
import json

# sum of the hash numbers up to 81 and if it falls within a specific range, we give it a note value
port = mido.open_output('test Bus 1')
# bpm_140 = [0.429, 0.214, 0.107]



def play_mido():
    while True:
        random_number = random.randint(10000000,99999999)
        print(random_number)
        time.sleep(0.429)

        note = sum([int(i) for i in str(random_number)])

        if note >= 0 and note < 10:
            print(note)
            msg = mido.Message('note_on', note=37, channel=1) # channel 2 on ableton live
            port.send(msg)

            arp = mido.Message('note_on', note=52, channel=4) # channel 3 on ableton live
            port.send(arp)

            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=52, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        if note >= 10 and note < 15:
            msg = mido.Message('note_on', note=38, channel=1) # channel 2 on ableton live
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=53, channel=4) # channel 3 on ableton live
            port.send(arp)

            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=53, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        elif note >= 15 and note < 20:
            msg = mido.Message('note_on', note=39, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=54, channel=4) # channel 3 on ableton live
            port.send(arp)


            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=54, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        elif note >= 20 and note < 25:
            msg = mido.Message('note_on', note=40, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(arp)

            
            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        elif note >= 25 and note < 30:

            msg = mido.Message('note_on', note=41, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=56, channel=4) # channel 3 on ableton live
            port.send(arp)

            
            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=56, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        elif note >= 30 and note < 35:
            msg = mido.Message('note_on', note=42, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=57, channel=4) # channel 3 on ableton live
            port.send(arp)

            
            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=57, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        elif note >= 35 and note < 40:
            msg = mido.Message('note_on', note=43, channel=0) # channel 1 on ableton live, Drum Rack
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=58, channel=4) # channel 3 on ableton live
            port.send(arp)

            
            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=58, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        else:
            msg = mido.Message('note_on', note=44, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=59, channel=4) # channel 3 on ableton live
            port.send(arp)

            
            time.sleep(0.429)

            arp_stop = mido.Message('note_off', note=59, channel=4) # channel 3 on ableton live
            port.send(arp_stop)



# with open('test.json') as f:
#     data = json.load(f)

play_mido()

# @app.route('/postjson', methods = ["POST"])
# def show_post():
#     # show the post with the given id, the id is an integer
#     print (request.is_json)
#     content = request.get_json()
#     # print (content)
#     play_mido(content)
#     return 'JSON posted'


# app.run(host='localhost', port= 3000)







## DRUM SECTION
# for x in range(0, 1000):
#     note = 40
#     note_2 = 37
#     # note = random.randint(33, 48)
#     # note_2 = random.randint(33, 48)
#     vel = random.randint(0, 100)
#     vel_2 = random.randint(0, 100)

#     port.send(mido.Message('note_on', 
#                             note=note, 
#                             velocity=vel, 
#                             channel=1))
#     print(note, vel)
#     time.sleep(0.6)

#     port.send(
#         mido.Message(
#             'note_on',
#             note=note,
#             velocity=vel,
#             channel=1
#         ))
#     print(note, vel)
#     time.sleep(0.2)

#     port.send(mido.Message('note_on', 
#                             note=note_2, 
#                             velocity=vel_2, 
#                             channel=1))
#     print(note_2, vel_2)
#     time.sleep(0.4)
    
#     port.send(
#         mido.Message(
#             'note_on',
#             note=note,
#             velocity=vel,
#             channel=1
#         ))
#     print(note, vel)
#     time.sleep(0.8)

#     port.send(
#         mido.Message(
#             'note_on',
#             note=note,
#             velocity=vel,
#             channel=1
#         ))
#     print(note, vel)
#     time.sleep(0.4)

#     port.send(mido.Message('note_on', 
#                             note=note_2, 
#                             velocity=vel_2, 
#                             channel=1))
#     print(note_2, vel_2)
#     time.sleep(0.8)

# mid = mido.MidiFile('song.mid')
# for msg in mid.play():
#     port.send(msg)