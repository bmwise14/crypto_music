import mido
import time
import random
import json

from flask import Flask, request, jsonify
app = Flask(__name__)

# sum of the hash numbers up to 81 and if it falls within a specific range, we give it a note value
port = mido.open_output('test Bus 1')
bpm_140 = [0.429, 0.214, 0.107]

def play_mido(data):
    # with open('test.json') as f:
    #     data = json.load(f)

    numbers = []
    numbers.append(data['hash'])

    for number in numbers:
        note = sum([int(i) for i in str(number)])

        if note >= 0 and note < 10:
            print(note)
            msg = mido.Message('note_on', note=37, channel=1) # channel 2 on ableton live
            port.send(msg)

            arp = mido.Message('note_on', note=52, channel=4) # channel 3 on ableton live
            port.send(arp)
            new = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(new)

            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=37, channel=1) # channel 2 on ableton live
            port.send(msg_stop)

            # arp_stop = mido.Message('note_off', note=52, channel=4) # channel 3 on ableton live
            # port.send(arp_stop)
            # new_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            # port.send(new_stop)


        if note >= 10 and note < 15:
            msg = mido.Message('note_on', note=38, channel=1) # channel 2 on ableton live
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=52, channel=4) # channel 3 on ableton live
            port.send(arp)
            new = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(new)

            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=38, channel=1) # channel 2 on ableton live
            port.send(msg_stop)

            # arp_stop = mido.Message('note_off', note=52, channel=4) # channel 3 on ableton live
            # port.send(arp_stop)
            # new_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            # port.send(new_stop

        elif note >= 15 and note < 20:
            msg = mido.Message('note_on', note=39, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=48, channel=4) # channel 3 on ableton live
            port.send(arp)
            new = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(new)


            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=39, channel=1) # channel 2 on ableton live
            port.send(msg_stop)

            # arp_stop = mido.Message('note_off', note=48, channel=4) # channel 3 on ableton live
            # port.send(arp_stop)
            # new_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            # port.send(new_stop)


        elif note >= 20 and note < 25:
            msg = mido.Message('note_on', note=40, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=52, channel=4) # channel 3 on ableton live
            port.send(arp)
            new = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(new)

            
            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=40, channel=1) # channel 2 on ableton live
            port.send(msg_stop)


            # arp_stop = mido.Message('note_off', note=52, channel=4) # channel 3 on ableton live
            # port.send(arp_stop)
            # new_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            # port.send(new_stop)

        elif note >= 25 and note < 30:

            msg = mido.Message('note_on', note=41, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(arp)

            
            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=41, channel=1) # channel 2 on ableton live
            port.send(msg_stop)

            arp_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            port.send(arp_stop)
        elif note >= 30 and note < 35:
            msg = mido.Message('note_on', note=42, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=52, channel=4) # channel 3 on ableton live
            port.send(arp)
            new = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(new)

            
            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=42, channel=1) # channel 2 on ableton live
            port.send(msg_stop)


            # arp_stop = mido.Message('note_off', note=52, channel=4) # channel 3 on ableton live
            # port.send(arp_stop)
            # new_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            # port.send(new_stop)

        elif note >= 35 and note < 40:
            msg = mido.Message('note_on', note=43, channel=0) # channel 1 on ableton live, Drum Rack
            print(note)
            port.send(msg)


            arp = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(arp)
            new = mido.Message('note_on', note=48, channel=4) # channel 3 on ableton live
            port.send(new)

            
            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=43, channel=1) # channel 2 on ableton live
            port.send(msg_stop)


            # arp_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            # port.send(arp_stop)
            # new_stop = mido.Message('note_off', note=48, channel=4) # channel 3 on ableton live
            # port.send(new_stop)
        else:
            msg = mido.Message('note_on', note=44, channel=1)
            print(note)
            port.send(msg)

            arp = mido.Message('note_on', note=48, channel=4) # channel 3 on ableton live
            port.send(arp)
            new = mido.Message('note_on', note=55, channel=4) # channel 3 on ableton live
            port.send(new)

            
            time.sleep(0.429)

            msg_stop = mido.Message('note_off', note=44, channel=1) # channel 2 on ableton live
            port.send(msg_stop)


            # arp_stop = mido.Message('note_off', note=48, channel=4) # channel 3 on ableton live
            # port.send(arp_stop)
            # new_stop = mido.Message('note_off', note=55, channel=4) # channel 3 on ableton live
            # port.send(new_stop)


@app.route('/postjson', methods = ["POST"])
def show_post():
    # show the post with the given id, the id is an integer
    print (request.is_json)
    content = request.get_json()
    play_mido(content)
    time.sleep(5000)
    return 'okay'


app.run(host='localhost', port= 3000)