import mido
import time
import random
import json

import rtmidi




midi_out = rtmidi.MidiOut()
midi_out.open_virtual_port('test Bus 1')




from flask import Flask, request, jsonify
app = Flask(__name__)

# sum of the hash numbers up to 81 and if it falls within a specific range, we give it a note value

# c = midi.MidiConnector('test Bus 1')

port = mido.open_output('test Bus 1')

# port.send(mido.Message('note_on', note=20, channel=1))

# port.send(mido.Message('note_off', note=20, channel=1))

# port.send(mido.Message('note_on', note=10, channel=1, time=96))
# port.send(mido.Message('note_on', note=15, channel=1))

# port.send(mido.Message('note_off', note=10, channel=1))
port.send(mido.Message('note_on', note=25, channel=1))
# port.send(mido.Message('note_on', note=30, channel=1))
# port.send(mido.Message('note_on', note=35, channel=1))
# port.send(mido.Message('note_on', note=40, channel=1))
# port.send(mido.Message('note_on', note=45, channel=1))
# port.send(mido.Message('note_on', note=50, channel=1))
# port.send(mido.Message('note_on', note=55, channel=1))
