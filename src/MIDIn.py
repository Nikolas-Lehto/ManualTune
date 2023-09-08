import mido
import numpy as np



# MIDI to frequency conversion function
def midi_to_frequency(note_number):
    return 440.0 * (2 ** ((note_number - 69) / 12.0))

def getMIDI(DeviceName):

    # Set up MIDI input
    midi_in = mido.open_input(DeviceName)
    for msg in midi_in.iter_pending():
        if msg.type == 'note_on':
            foo = midi_to_frequency(msg.note)
            output(True, foo)
        else:
            output(False, None)
    return output
