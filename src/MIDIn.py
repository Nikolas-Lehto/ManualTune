import mido
import numpy as np
import os

# MIDI to frequency conversion function
def midi_to_frequency(note_number:int):
    return 440.0 * (2 ** ((note_number - 69) / 12.0))

def ChooseMIDI(MIDI_framework:str="rtmidi"):

    mido.set_backend(MIDI_framework)
    while True:
        os.system('clear')
        # Fetch available MIDI devices
        MIDIlist = mido.get_input_names()

        #Loop through MIDI devices and print them out
    
        for i in MIDIlist:
            print(i + ' ' + MIDIlist[i])

        #Ask the user to choose a device

        try:
            bar = int(input('Please choose a MIDI device (Press enter to refresh): '))
            return MIDIlist[bar]
        except KeyboardInterrupt:
            print()
            print('CTRL+C pressed. Exiting...')
            return 1
        except:
            print('Please input valid integer')
            continue

def getMIDI(DeviceName:str):

    # Set up MIDI input
    midi_in = mido.open_input(DeviceName)
    for msg in midi_in.iter_pending():
        if msg.type == 'note_on':
            foo = midi_to_frequency(msg.note)
            output(True, foo)
        else:
            output(False, None)
    return output
