#!/usr/bin/env python3

import isobar as iso
import logging
import time

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

def print_message(message):
    print("INCOMING MIDI: %s" % message)


# def estart():
#     print("STARTNIG")
#     print(timeline)
#     timeline.background()

#def estop():
#    print("STOPPING")
#    for device in timeline.output_devices:
#        device.all_notes_off()
#        device.stop()
#    #timeline.clock_source.stop()

# timeline.start = estart
# timeline.stop = estop

midi_in = iso.MidiInputDevice()
# midi_in.callback = print_message

timeline = iso.Timeline(clock_source=midi_in)
timeline.schedule({
    "note": iso.PSequence([60, 67, 72, 77]),
    "amplitude": iso.PWhite(0, 128)
})

timeline.run()

while 1:
    time.sleep(1.0)

