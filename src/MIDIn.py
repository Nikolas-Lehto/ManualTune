import mido
import numpy as np
import os

class MIDI():
    def __init__(self, MIDI_framework:str="rtmidi", device:int=0):
        self.device = device
        mido.set_backend(MIDI_framework)

    def midi_to_frequency(self,note_number:int):
        """A MIDI to frequency conversion function."""
        return 440.0 * (2 ** ((note_number - 69) / 12.0))

    def ChooseDevice(self):
        """A simple CLI to select a midi device."""
        while True:
            os.system('clear')
            # Fetch available MIDI devices
            DeviceList = mido.get_input_names()

            #Loop through MIDI devices and print them out
            for i in range(len(DeviceList)):
                print(f'{i} {DeviceList[i]}')

            #Ask the user to choose a device
            try:
                self.device = int(input('Please choose a MIDI device (Press enter to refresh): '))
                return MIDIlist[self.device]
            except KeyboardInterrupt:
                print()
                print('CTRL+C pressed. Exiting...')
                return 1
            except:
                print('Please input valid integer')
                continue

    def ListDevices(self):
        """Return a list of MIDI devicesin a machine readable (device index, device name) form."""
        Devices = mido.get_input_names()
        self.DeviceList =[]
        for i in range(len(Devices)):
            DeviceList.append(({i},{Devices[i]}))
        return self.DeviceList

    def SetDevice(self, device:int=0):
        """Set the MIDI device"""
        self.device = device

    def GetInputs(self,Device:int=0):
        # Set up MIDI input
        midi_in = mido.open_input(Device)
        self.msgs = []
        for msg in midi_in.iter_pending():
            match msg.type:
                case 'note_on':
                    self.msgs.append((True, msg))
                case 'note_off':
                    self.msgs.remove((True, msg))                
                case _:
                    pass
            if self.msgs != []:
                return self.msgs
            else:
                return (False, None)
            
