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

            msg = mido.Message('note_on', note=37, channel=1) # channel 2 on ableton live
            msg2 = mido.Message('note_on', note=37, channel=0) # channel 1 on ableton live
            msg3 = mido.Message('note_on', note=43, channel=2) # channel 3 on ableton live, G2
            print(note)
            port.send(msg3)
            time.sleep(0.429)
        if note >= 10 and note < 15:
            msg = mido.Message('note_on', note=37, channel=1) # channel 2 on ableton live
            msg2 = mido.Message('note_on', note=37, channel=0) # channel 1 on ableton live
            msg3 = mido.Message('note_on', note=43, channel=2) # channel 3 on ableton live, G2
            print(note)
            port.send(msg)
            port.send(msg2)
            port.send(msg3)
            time.sleep(0.429)
        elif note >= 15 and note < 20:

            msg = mido.Message('note_on', note=40, channel=1)
            msg2 = mido.Message('note_on', note=37, channel=0) # channel 1 on ableton live
            msg3 = mido.Message('note_on', note=36, channel=2) # channel 3 on ableton live, C2
            print(note)
            port.send(msg)
            port.send(msg2)
            port.send(msg3)
            time.sleep(0.429)
        elif note >= 20 and note < 25:

            msg = mido.Message('note_on', note=40, channel=1)
            msg2 = mido.Message('note_on', note=37, channel=0) # channel 1 on ableton live
            msg3 = mido.Message('note_on', note=36, channel=2) # channel 3 on ableton live, C2
            print(note)
            port.send(msg)
            port.send(msg2)
            port.send(msg3)
            time.sleep(0.429)
        elif note >= 25 and note < 30:

            msg = mido.Message('note_on', note=40, channel=1)
            msg2 = mido.Message('note_on', note=37, channel=0) # channel 1 on ableton live
            msg3 = mido.Message('note_on', note=36, channel=2) # channel 3 on ableton live, C2
            print(note)
            port.send(msg)
            port.send(msg2)
            port.send(msg3)
            time.sleep(0.429)
        elif note >= 30 and note < 35:

            msg = mido.Message('note_on', note=40, channel=1)
            msg2 = mido.Message('note_on', note=37, channel=0) # channel 1 on ableton live
            msg3 = mido.Message('note_on', note=36, channel=2) # channel 3 on ableton live, C2
            print(note)
            port.send(msg)
            port.send(msg2)
            port.send(msg3)
            time.sleep(0.429)
        elif note >= 35 and note < 40:

            msg = mido.Message('note_on', note=40, channel=0) # channel 1 on ableton live, Drum Rack
            msg2 = mido.Message('note_on', note=37, channel=1)  # Audio rack
            msg3 = mido.Message('note_on', note=36, channel=2) # channel 3 on ableton live, C2
            print(note)
            port.send(msg)
            # port.send(msg2)
            port.send(msg3)
            time.sleep(0.429)
        else:

            msg = mido.Message('note_on', note=40, channel=1)
            msg2 = mido.Message('note_on', note=37, channel=0) # channel 1 on ableton live
            msg3 = mido.Message('note_on', note=36, channel=2) # channel 3 on ableton live, C2
            print(note)
            port.send(msg)
            port.send(msg2)
            port.send(msg3)
            time.sleep(0.429)



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